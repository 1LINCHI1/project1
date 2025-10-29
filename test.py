def main():
	print("example")
	print("example1")
	print("example2")
	print("example3")
	print("example4")

	while True:
		command = input(">>>").strip().lower()

		if command == "exit":
			print("bye")
			break
		elif command == "a":
			import nmap
			print("nmap is ready")
			host = input("host:")
			nm = nmap.PortScanner()
			nm.scan(host, '22-443')
			nm.command_line()
			f'nmap -oX - -p 22-443 -sV {host}'
			nm.scaninfo()




if __name__ == "__main__":
	main()