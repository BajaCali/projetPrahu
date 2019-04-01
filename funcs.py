def get_stop_id_by_name(name, stops): # returns <stop_id> from name of the stop
	for stop in stops:
		if (stop["stop_name"] == name):
			return stop["stop_id"]
	return None


def get_trip_ids_by_stop_id(stop_id, stop_times, trips_data): # returns list of <trip_id>s and <route_id>s which stops at the stop with given stop_id
	trip_ids = []
	route_ids = []
	for trip in trips:
		if (stop_id == trip["stop_id"]):
			trip_ids.append(trip["trip_id"])
			route_ids.append(get_route_id_by_trip_id(trip["trip_id"], trips_data))
	if (trip_ids == []):
		trip_ids = None
	if (route_ids == []):
		route_ids = None
	return trip_ids, route_ids


def get_route_id_by_trip_id(trip_id, trips): # returns <route_id> of given trip_id
	for trip in trips:
		if (trip_id == trip['trip_id']):
			return trip['route_id']
	return None


def get_stop_ids_with_times_by_trip_id(trip_id, stop_times): # returns dict, where value is list with times and keys are <stop_id>s
	stop_ids_with_times = {}
	for i in range(len(stop_times)):
		if stop_times[i+1]['trip_id'] == trip_id:
			if stop_times[i+1]['stop_id'] not in stop_ids_with_times.keys():
				stop_ids_with_times[stop_times[i+1]['stop_id']] = []
			stop_ids_with_times[stop_times[i+1]['stop_id']].append(stop_times[i+1]['departure_time'])
	if not stop_ids_with_times:
		return None
	return stop_ids_with_times


def get_time(trip_id, stop_id, stop_times): # returns (arrival_time, departure_time) on given <stop_id> and <trip_id>
	for time in stop_times:
		if (time['stop_id'] == stop_id and time['trip_id'] == trip_id):
			return (time['arrival_time'], time['departure_time'])
	return None


def get_times(trip_ids, stop_id, stop_times): # retrun list of tuples of times on given <stop_id> and list of trip_ids
	return [get_time(trip, stop_id, stop_times) for trip in trip_ids]


def get_next_stop_with_times(trips_ids, stop_id, stop_times):
	return (stop_id, get_times(trip_ids, stop_id, stop_times))

# todo:
# f(zastavka) -> [linky] and [trips]
# g(zastavka, trips) -> [next_stops]
# h(linka, zastavka, trips) -> [casy]
