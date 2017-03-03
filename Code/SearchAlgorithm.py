# This file contains all the required routines to make an A* search algorithm.
#
__authors__='Diego Velazquez Dorta, Yael Tudela Barroso, Qiang Chen'
__group__='DX18.03'
# _________________________________________________________________________________________
# Intel.ligencia Artificial
# Grau en Enginyeria Informatica
# Curs 2016- 2017
# Universitat Autonoma de Barcelona
# _______________________________________________________________________________________

from SubwayMap import *
from SubwayMap import *
import math as m


class Node:
    # __init__ Constructor of Node Class.
    def __init__(self, station, father):
        """
        __init__: 	Constructor of the Node class
        :param
                - station: STATION information of the Station of this Node
                - father: NODE (see Node definition) of his father
        """
        
        self.station = station      # STATION information of the Station of this Node
        self.g = 0                  # REAL cost - depending on the type of preference -
                                    # to get from the origin to this Node
        self.h = 0                 # REAL heuristic value to get from the origin to this Node
        self.f = 0                  # REAL evaluate function
        if father ==None:
			self.parentsID=[]
        else:
			self.parentsID = [father.station.id]
			self.parentsID.extend(father.parentsID)         # TUPLE OF NODES (from the origin to its father)
        self.father = father                                 # NODE pointer to his father
        self.time = 0               # REAL time required to get from the origin to this Node
                                    # [optional] Only useful for GUI
        self.num_stopStation = 0    # INTEGER number of stops stations made from the origin to this Node
                                    # [optional] Only useful for GUI
        self.walk = 0               # REAL distance made from the origin to this Node
                                    # [optional] Only useful for GUI
        self.transfers = 0          # INTEGER number of transfers made from the origin to this Node
                                    # [optional] Only useful for GUI


    def setEvaluation(self):
        """
        setEvaluation: 	Calculates the Evaluation Function. Actualizes .f value
       
        """
        
        self.f = self.g + self.h
        
    def setHeuristic(self, typePreference,  node_destination, city):
        """"
        setHeuristic: 	Calculates the heuristic depending on the preference selected
        :params
                - typePreference: INTEGER Value to indicate the preference selected: 
                                0 - Null Heuristic
                                1 - minimum Time
                                2 - minimum Distance 
                                3 - minimum Transfers
                                4 - minimum Stops
                - node_destination: PATH of the destination station
                - city: CITYINFO with the information of the city (see CityInfo class definition)
        """
        
        #Time Preference
        if typePreference == 1:
            distance1 = (self.station.x - node_destination.station.x)**2
            distance2 = (self.station.y - node_destination.station.y)**2
            
            self.h = m.sqrt(distance1 + distance2)/city.max_velocity       
        
            if self.station.line != node_destination.station.line:
                self.h += city.min_transfer
        
        #Distance Preference        
        elif typePreference == 2:
            distance1 = (self.station.x - node_destination.station.x)**2
            distance2 = (self.station.y - node_destination.station.y)**2
            
            self.h = m.sqrt(distance1 + distance2)
           
        #Transfers Preference
        elif typePreference == 3: 
           if self.station.line != node_destination.station.line:
                self.h = 1
           else:
               self.h = 0
        
        #Stops Preference
        elif typePreference == 4:
            if self.station.name == node_destination.station.name:
                self.h = 0
            else:
                self.h = 1
        
        #Null heuristic
        else:
            self.h = None        
        
            
                

    def setRealCost(self, costTable):
        """
        setRealCost: 	Calculates the real cost depending on the preference selected
        :params
                 - costTable: DICTIONARY. Relates each station with their adjacency and their real cost. NOTE that this
                             cost can be in terms of any preference.
        """
       
        if self.father != None:              
              self.g = costTable[self.father.station.id][self.station.id]+self.father.g 
        



def Expand(fatherNode, stationList, typePreference, node_destination, costTable,city):
     """
        Expand: It expands a node and returns the list of connected stations (childrenList)
        :params
                - fatherNode: NODE of the current node that should be expanded
                - stationList: LIST of the stations of a city. (- id, destinationDic, name, line, x, y -)
                - typePreference: INTEGER Value to indicate the preference selected:
                                0 - Null Heuristic
                                1 - minimum Time
                                2 - minimum Distance
                                3 - minimum Transfers
                                4 - minimum Stops
                - node_destination: NODE (see Node definition) of the destination
                - costTable: DICTIONARY. Relates each station with their adjacency an their real cost. NOTE that this
                             cost can be in terms of any preference.
                - city: CITYINFO with the information of the city (see CityInfo class definition)
        :returns
                - childrenList:  LIST of the set of child Nodes for this current node (fatherNode)

    """
    
    



def RemoveCycles(childrenList):
    """
        RemoveCycles: It removes from childrenList the set of childrens that include some cycles in their path.
        :params
                - childrenList: LIST of the set of child Nodes for a certain Node
        :returns
                - listWithoutCycles:  LIST of the set of child Nodes for a certain Node which not includes cycles
    """




def RemoveRedundantPaths(childrenList, nodeList, partialCostTable):
    """
        RemoveRedundantPaths:   It removes the Redundant Paths. They are not optimal solution!
                                If a node is visited and have a lower g in this moment, TCP is updated.
                                In case of having a higher value, we should remove this child.
                                If a node is not yet visited, we should include to the TCP.
        :params
                - childrenList: LIST of NODES, set of childs that should be studied if they contain rendundant path
                                or not.
                - nodeList : LIST of NODES to be visited
                - partialCostTable: DICTIONARY of the minimum g to get each key (Node) from the origin Node
        :returns
                - childrenList: LIST of NODES, set of childs without rendundant path.
                - nodeList: LIST of NODES to be visited updated (without redundant paths)
                - partialCostTable: DICTIONARY of the minimum g to get each key (Node) from the origin Node (updated)
    """



def sorted_insertion(nodeList,childrenList):
	""" Sorted_insertion: 	It inserts each of the elements of childrenList into the nodeList.
							The insertion must be sorted depending on the evaluation function value.
							
		: params:
			- nodeList : LIST of NODES to be visited
			- childrenList: LIST of NODES, set of childs that should be studied if they contain rendundant path
                                or not.
		:returns
                - nodeList: sorted LIST of NODES to be visited updated with the childrenList included 
	"""


def setCostTable( typePreference, stationList,city):
    """
    setCostTable :      Real cost of a travel.
    :param
            - typePreference: INTEGER Value to indicate the preference selected:
                                0 - Adjacency
                                1 - minimum Time
                                2 - minimum Distance
                                3 - minimum Transfers
                                4 - minimum Stops
            - stationList: LIST of the stations of a city. (- id, destinationDic, name, line, x, y -)
            - city: CITYINFO with the information of the city (see CityInfo class definition)
    :return:
            - costTable: DICTIONARY. Relates each station with their adjacency an their g, depending on the
                                 type of Preference Selected.
    """

    if typePreference == 0:
        return city.adjacency
    
    costTable = {}
    for origin in city.adjacency.keys():
        costTable[origin] = {}
        for dest in city.adjacency[origin].keys():
            
            if typePreference == 1:
                # Returns real cost in time from origin to dest        
                costTable[origin][dest] = stationList[origin - 1].destinationDic[dest]
            
            elif typePreference == 2:
                # We consider line trasnfers within a same station to have a distance of 0
                if stationList[origin - 1].name == stationList[dest - 1].name:
                    costTable[origin][dest] = 0             
                else:             
                    # Returns real cost in distance from origin to dest
                    time = stationList[origin - 1].destinationDic[dest]
                    costTable[origin][dest] = city.velocity_lines[stationList[origin - 1].line -1] * time
                
            elif typePreference == 3:
                #Returns real cost in number of transfers from orgin to dest
                if stationList[origin - 1].line != stationList[dest -1].line:
                    costTable[origin][dest] = 1    
                else:
                    costTable[origin][dest] = 0
                             
            else:
                #Returns real cost in number of stops from orgin to dest
                if stationList[origin - 1].name != stationList[dest -1].name:
                    costTable[origin][dest] = 1
                    
                else:
                    costTable[origin][dest] = 0
                
    return costTable
            
def coord2station(coord, stationList):
    """
    coord2station :      From coordinates, it searches the closest station.
    :param
            - coord:  LIST of two REAL values, which refer to the coordinates of a point in the city.
            - stationList: LIST of the stations of a city. (- id, destinationDic, name, line, x, y -)

    :return:
            - possible_origins: List of the Indexes of the stationList structure, which corresponds to the closest
            station
    """


def AstarAlgorithm(stationList, coord_origin, coord_destination, typePreference,city,flag_redundants):
    """
     AstarAlgorithm: main function. It is the connection between the GUI and the AStar search code.
     INPUTS:
            - stationList: LIST of the stations of a city. (- id, name, destinationDic, line, x, y -)
            - coord_origin: TUPLE of two values referring to the origin coordinates
            - coord_destination: TUPLE of two values referring to the destination coordinates
            - typePreference: INTEGER Value to indicate the preference selected:
                                0 - Adjacency
                                1 - minimum Time
                                2 - minimum Distance
                                3 - minimum Transfers
                                4 - minimum Stops
            - city: CITYINFO with the information of the city (see CityInfo class definition)
			- flag_redundants: [0/1]. Flag to indicate if the algorithm has to remove the redundant paths (1) or not (0)
			
    OUTPUTS:
            - time: REAL total required time to make the route
            - distance: REAL total distance made in the route
            - transfers: INTEGER total transfers made in the route
            - stopStations: INTEGER total stops made in the route
            - num_expanded_nodes: INTEGER total expanded nodes to get the optimal path
            - depth: INTEGER depth of the solution
            - visitedNodes: LIST of INTEGERS, IDs of the stations corresponding to the visited nodes
            - idsOptimalPath: LIST of INTEGERS, IDs of the stations corresponding to the optimal path
            (from origin to destination)
            - min_distance_origin: REAL the distance of the origin_coordinates to the closest station
            - min_distance_destination: REAL the distance of the destination_coordinates to the closest station
            


            EXAMPLE:
            return optimalPath.time, optimalPath.walk, optimalPath.transfers,optimalPath.num_stopStation,
            len(expandedList), len(idsOptimalPath), visitedNodes, idsOptimalPath, min_distance_origin,
            min_distance_destination
    """

    

