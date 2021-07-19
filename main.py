import speedtest

st = speedtest.Speedtest()

print("Loading servers...")
st.get_servers() # get list of servers

print("Choosing best server...")
best = st.get_best_server() # choose best server
print(f"Found: {best['host']} located in {best['country']}")

print("Performing download test...")
download_result = st.download()
print("Performing upload test...")
upload_result = st.upload()
ping_result = st.results.ping

print(f"Download Speed: {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"Upload Speed: {upload_result / 1024 / 1024:.2f} Mbit/s")
print(f"Ping: {ping_result:.2f} ms")

