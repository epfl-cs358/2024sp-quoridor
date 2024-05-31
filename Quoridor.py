# ==== DON'T CHANGE AFTER THIS LINE ====
from collections import deque


import serial
import time
from computer_vision.get_board_state import *

def greedy_quoridor_solver(bot_node, player_node, board_walls, debug = False):
    edges = {}
    free_walls = []
    
    def printGraph(g_edges):
        for y in range(0, 9):
            for x in range(0, 9):
                print(convertToId(x,y), ":", g_edges[convertToId(x, y)])

    def copyGraph(g_edges):
        new_edges = {}
        for x in range (0, 9):
            for y in range(0, 9):
                edges_for_node = {"right":[], "left":[], "up":[], "down":[]}
                if(g_edges[convertToId(x,y)]["left"] != []):
                    edges_for_node["left"] = g_edges[convertToId(x,y)]["left"]
                if(g_edges[convertToId(x,y)]["right"] != []):
                    edges_for_node["right"] = g_edges[convertToId(x,y)]["right"]
                if(g_edges[convertToId(x,y)]["up"] != []):
                    edges_for_node["up"] = g_edges[convertToId(x,y)]["up"]  
                if(g_edges[convertToId(x,y)]["down"] != []):
                    edges_for_node["down"] = g_edges[convertToId(x,y)]["down"] 
                new_edges[convertToId(x, y)] = edges_for_node
        return new_edges       

    def convertToId(x, y):
        return y * 10 + x 

    def canWallBePlaced(g_edges, wall):
        if(0 <=(wall[0] % 10) <= 7 and 0 <= (wall[0] // 10) <= 7):
            if(wall[1] == "HORIZONTAL" and 
               g_edges[wall[0]]["up"] != [] and 
               g_edges[wall[0] + 1]["up"] != [] and 
               g_edges[wall[0] + 10]["down"] != [] and 
               g_edges[wall[0] + 11]["down"] != []):
                return True
            elif(wall[1] == "VERTICAL" and 
                 g_edges[wall[0]]["right"] != [] and 
                 g_edges[wall[0] + 1]["left"] != [] and 
                 g_edges[wall[0] + 10]["right"] != [] and 
                 g_edges[wall[0] + 11]["left"] != []):
                return True
        return False    

    def addWall(g_edges, wall):
        if(wall[1] == "HORIZONTAL"):
            g_edges[wall[0]]["up"] = []
            g_edges[wall[0] + 1]["up"] = []
            g_edges[wall[0] + 10]["down"] = []            
            g_edges[wall[0] + 11]["down"] = []
        else: 
            g_edges[wall[0]]["right"] = []
            g_edges[wall[0] + 1]["left"] = []
            g_edges[wall[0] + 10]["right"] = []
            g_edges[wall[0] + 11]["left"] = []    

    def initGraph(walls):
        for x in range (0, 9):
            for y in range(0, 9):
                edges_for_node = {"right":[], "left":[], "up":[], "down":[]}
                if(x != 0):
                    edges_for_node["left"] = convertToId(x-1, y)
                if(x != 8):
                    edges_for_node["right"] = convertToId(x+1, y)
                if(y != 8):
                    edges_for_node["up"] = convertToId(x, y+1)    
                if(y != 0):
                    edges_for_node["down"] = convertToId(x, y-1)  
                edges[convertToId(x, y)] = edges_for_node
        for wall in walls:
            if(wall[0] % 10 == 8):
                free_walls.append(wall)
            else:
                addWall(edges, wall)

    def win_for_bot(node):
        return node // 10 == 8

    def win_for_player(node):
        return node // 10 == 0


    def shortest_path_to_win(start_node, g_edges, win_condition):
        visited_nodes = set()
        queue = deque([(start_node, [start_node])])

        while queue:
            node, path = queue.popleft()
            if win_condition(node):
                return path
            visited_nodes.add(node)
            neighbors = [
                g_edges[node]["right"],
                g_edges[node]["left"],
                g_edges[node]["up"],
                g_edges[node]["down"]]
            for neighbor in neighbors:
                if(neighbor != [] and neighbor not in visited_nodes):
                     queue.append((neighbor, path + [neighbor]))
        return None

    initGraph(board_walls)

    if(win_for_bot(bot_node) or win_for_player(player_node)):
        return None

    bot_path = shortest_path_to_win(bot_node, edges, win_for_bot)
    player_path = shortest_path_to_win(player_node, edges, win_for_player)
    
    if(debug):
        print(bot_path)
        print(player_path)

    if(len(bot_path) <= len(player_path) or free_walls == []):
        if(bot_path[1] == player_path[0]):
            return "<{}><{}><PLAYER>".format(bot_path[0], bot_path[2])
        else:
            return "<{}><{}><PLAYER>".format(bot_path[0], bot_path[1])
    else:
        best_winning_move = (free_walls[0], bot_path, player_path)
        best_losing_move = (free_walls[0], bot_path, player_path)
        for i in range(len(player_path) - 1):
            cur_node = player_path[i]
            next_node = player_path[i+1]
            walls = []
            if(edges[cur_node]["right"] == next_node):
                wall = (cur_node, "VERTICAL")
                if(canWallBePlaced(edges, wall)):
                    walls.append(wall)

                wall = (cur_node - 10, "VERTICAL")
                if(canWallBePlaced(edges, wall)):
                    walls.append(wall)
            elif(edges[cur_node]["left"] == next_node):
                wall = (next_node, "VERTICAL")
                if(canWallBePlaced(edges, wall)):
                    walls.append(wall)

                wall = (next_node - 10, "VERTICAL")
                if(canWallBePlaced(edges, wall)):
                    walls.append(wall)

            elif(edges[cur_node]["up"] == next_node):
                wall = (cur_node, "HORIZONTAL")
                if(canWallBePlaced(edges, wall)):
                    walls.append(wall)

                wall = (cur_node - 1, "HORIZONTAL")
                if(canWallBePlaced(edges, wall)):
                    walls.append(wall)

            elif(edges[cur_node]["down"] == next_node):
                wall = (next_node, "HORIZONTAL")
                if(canWallBePlaced(edges, wall)):
                    walls.append(wall)

                wall = (next_node - 1, "HORIZONTAL")
                if(canWallBePlaced(edges, wall)):
                    walls.append(wall)
            for wall in walls:
                new_edges = copyGraph(edges)
                addWall(new_edges, wall)

                new_bot_path = shortest_path_to_win(bot_node, new_edges, win_for_bot)
                new_player_path = shortest_path_to_win(player_node, new_edges, win_for_player)

                if(new_bot_path != None and new_player_path != None):
                    if(len(new_bot_path) <= len(new_player_path) and 
                       len(new_player_path) - len(new_bot_path) > len(best_winning_move[2]) - len(best_winning_move[1])):
                        best_winning_move = (wall, new_bot_path, new_player_path)
                    elif(len(new_bot_path) > len(new_player_path) and
                        len(new_bot_path) - len(new_player_path) <  len(best_losing_move[1]) - len(best_losing_move[2])):
                        best_losing_move = (wall, new_bot_path, new_player_path)

        if(debug):
            print(best_winning_move)
            print(best_losing_move) 
                        
        if(best_winning_move != (free_walls[0], bot_path, player_path)):
            return "<{}><{}><WALL><{}><{}>".format(free_walls[0][0], best_winning_move[0][0], free_walls[0][1], best_winning_move[0][1])
        else:
            return "<{}><{}><WALL><{}><{}>".format(free_walls[0][0], best_losing_move[0][0], free_walls[0][1], best_losing_move[0][1])       
# ==== DON'T CHANGE BEFORE THIS LINE ==== 

# ==== FREE WALL MEMORY MANAGEMENT ==== 
free_wall_mem = []
def init_free_walls():
    try:
        nb_free_walls = max(0, min(int(input("number of free walls: ")), 10))
    except ValueError:
        nb_free_walls = 10

    for i in range(10 - nb_free_walls, 10):
        free_wall_mem.append((10 * i + 8, "HORIZONTAL"))

import re
def remove_free_wall(move):
    if("WALL" in move):
        result = re.findall(r'\<.*?\>', move)
        position = int(result[0].replace('<', '').replace('>', ''))
        if(position % 10 == 8):
            free_wall_mem.remove((position, "HORIZONTAL"))

# ==== COMMUNICATION ====
def convertTupleToId(x, y):
    return y * 10 + x 
def convertWallTuplesToWalls(input, output):
    for wall in input:
        if(wall[1] == "H"):
            output.append((convertTupleToId(wall[0][0], wall[0][1]), "HORIZONTAL"))
        else:
            output.append((convertTupleToId(wall[0][0], wall[0][1]), "VERTICAL"))


ser = serial.Serial('COM6', 9600)
init_free_walls()
videoCapture = setup_camera()
time.sleep(5)

try:
    while True:
        # Read bytes from Arduino
        if ser.readable:
            received_bytes = ser.readline()
                
            # Check if any bytes were received
            if received_bytes:
                print("Received from Arduino: ", received_bytes.decode().rstrip('\n'))
                    
                if(received_bytes == b'Get next move\r\n'):
                    # # ==== MANAGING OF BOARD STATE ====

                    player_node_tuple, bot_node_tuple, board_walls_tuple = detect_pieces(videoCapture) 
                    bot_node = convertTupleToId(bot_node_tuple[0], bot_node_tuple[1])
                    player_node = convertTupleToId(player_node_tuple[0], player_node_tuple[1])
                    board_walls = []
                    print("Received from Camera: player ", player_node_tuple)
                    print("Received from Camera: bot ", bot_node_tuple)
                    print("Received from Camera: walls ", board_walls_tuple)
                    convertWallTuplesToWalls(board_walls_tuple, board_walls)
                    
                    response_message = greedy_quoridor_solver(bot_node, player_node, board_walls + free_wall_mem, False)
                    if response_message == None:
                        print("Someone won the game!")
                    else:    
                        # Send response to Arduino
                        sent_message = False
                        while(not(sent_message)):
                            if(ser.writable):
                                ser.write(response_message.encode())
                                sent_message = True
                                print("Message sent: ", response_message)
                                remove_free_wall(response_message)
        # Wait for a moment before sending next message
        time.sleep(1)
finally:
    ser.close()
    print("Failure")