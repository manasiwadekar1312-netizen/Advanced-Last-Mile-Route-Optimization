from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def solve_vrp(distance_matrix, num_vehicles=2, depot=0):
    manager = pywrapcp.RoutingIndexManager(
        len(distance_matrix), num_vehicles, depot
    )

    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return int(distance_matrix[from_node][to_node] * 1000)

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )

    solution = routing.SolveWithParameters(search_parameters)

    routes = []

    if solution:
        for vehicle_id in range(num_vehicles):
            index = routing.Start(vehicle_id)
            route = []
            while not routing.IsEnd(index):
                node = manager.IndexToNode(index)
                route.append(node)
                index = solution.Value(routing.NextVar(index))
            routes.append(route)

    return routes