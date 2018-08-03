def merge_the_tools(string, k):
	n = len(string)
	subsegments = n/k
	start = 0
	end = k
	for i in range(subsegments):
		t = string[start:end]
		u = list(t)
		e = list()
		for j in u:
			if j not in e:
				e.append(j)
		result = "".join(str(x) for x in e)
		print(result)
		start = end
		end = end+k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

