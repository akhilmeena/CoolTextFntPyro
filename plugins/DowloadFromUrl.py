#made by akhil
from plugins import helper

def get_size(size):
    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

def time_formatter(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + "d, ") if days else "")
        + ((str(hours) + "h, ") if hours else "")
        + ((str(minutes) + "m, ") if minutes else "")
        + ((str(seconds) + "s, ") if seconds else "")
        + ((str(milliseconds) + "ms, ") if milliseconds else "")
    )
    return tmp[:-2]


async def download_file(url,file_path, file_name, msg, start, bot):
  CHUNK_SIZE = 1024*6 # 2341
  downloaded = 0
  display_message = ""
  humanbytes = get_size
  async with requests.get(url) as response:
    total_length = int(response.headers["Content-Length"])
    content_type = response.headers["Content-Type"]
    if "text" in content_type and total_length < 500:
      return await response.release()
      await msg.edit(helper.DonloadFiletext.format(url,file_name,get_size(total_length))
      with open(file_path, 'wb') as f_handle:
        if total_length is None:
          f.write(response.content)
        else:
          while True:
          #for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
          #downloaded += len(data)
            chunk = await response.content.read(CHUNK_SIZE)
          #if not chunk:
            #break
            f_handle.write(chunk)
            downloaded += CHUNK_SIZE
            now = time.time()
            diff = now - start
            if round(diff % 10.00) == 0: #downloaded == total_length:
              percentage = downloaded * 100 / total_length
              speed = downloaded / diff
              elapsed_time = round(diff) * 1000
              time_to_completion = (round((total_length - downloaded) / speed) * 1000)
              estimated_total_time = elapsed_time + time_to_completion
              try:
                if total_length < downloaded:
                  total_length = downloaded
                  current_message = helper.DownloadingProgress.format("%.2f" % (percentage), url, file_name, humanbytes(total_length), humanbytes(downloaded), time_formatter(estimated_total_time))
                  if (current_message != display_message and current_message != "empty"):
                    print(current_message)
                    await msg.edit(current_message)
                  display_message = current_message
              except Exception as e:
                print("Error",e)
    return await response.release()
  return file_name