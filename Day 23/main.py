from supporting import PaginatedResults

pages = [
    ["server-01", "server-02", "server-03"],
    [],
    ["server-04", "server-05"],
    ["server-06", "server-07", "server-08"],
]

results = PaginatedResults(pages)

for server in results:
    print(server)

results = PaginatedResults(pages)

iterator = iter(results)

print(next(iterator))
print(next(iterator))
print(next(iterator))