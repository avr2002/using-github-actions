from type_hints import Duck     # noqa: E0402

duck = Duck()

# Now we can get auto completion by using stubs
duck.quack()

duck.swim()
