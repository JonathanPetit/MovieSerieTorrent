database = {
  "season": "([Ss]?[0-9]{1,2})[Eex]",
  "episode": "([Eex][0-9]{1,2})",
  "year": "[\\[\\(]?((?:19[0-9]|20[012])[0-9])[\\]\\)]?",
  "languages": "FRENCH|French|french|TRUEFRENCH|VOSTFR|VOST",
  "sites": "[\\[\\s]{0,2}([Ww]{3}[.][A-Za-z0-9]+[.][a-z]{2,3})[\\]\\s]{0,2}",
  "codec": "XViD|XVID|xvid|Xvid|XviD|x264|h\\.?264",
  "quality": "((?:DVD|HD|B[Rr]|BD|WEB)[RrIiPp]{3}|[HP]DTV|H?D?CAM|[Bb]lu[Rr]ay|DVDSCR|WEB-DL)",
  "resolution": "([0-9]{3,4}p)",
  "audio": "(MP3|DD5\\.?1|Dual[\\- ]Audio|LiNE|DTS|AAC(?:\\.?2\\.0)?|AC3(?:\\.5\\.1)?)",
  "sub": "FASTSUB|FANSUB",
  "group": "[\\s]{2,}([A-Za-z0-9]+$)",
  "extension": "[\\s]{0,1}(avi|mkv)$"
}
