<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
<form action="\write" method="post">
	diaryInput: <input name="diaryInput" type="text" id="inp" />
    <input value="Submit" type="submit" />
	<button name="quit" onclick="close();">All Done</button>
</form>
	<textarea cols=50 rows=50 id="ta">{{diaryWritten}}
	</textarea>
</body>