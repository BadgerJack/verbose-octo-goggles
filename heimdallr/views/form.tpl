<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>Welcome to Heimdallr</title>
	<link rel="stylesheet" href="style.css" type="text/css"/>
</head>

<body>
	<div id="header">
		<div align="left"><a href="/" id="logo"><img src="heimdall_icon_edited.png" alt="LOGO" /></a></div>
	</div> <!-- /#header -->
	<div id="content">
		<div class="body">
			<div class="details">
				<p>

					<form class="form-horizontal" action="/vote" method="post">
					<fieldset>

					<!-- Form Name -->
					<!--<legend>Voting Platform</legend>-->

					<!-- Text input-->
					<div class="form-group">
					  <label class="col-md-4 control-label" for="Name">Voter ID</label>
					  <div class="col-md-4">
					  <input name="voterID" type="text" placeholder="placeholder" value="{{randnum}}"required="" readonly>
					  </div>
					</div>
					<br>

					<!-- Multiple Radios -->
					<div class="form-group">
					  <label class="col-md-4 control-label" for="radios">Ballot Options</label>
					  <div class="col-md-4">
					  <div class="radio">
						<label for="radios-0">
						  <input type="radio" name="ballot" id="Maria Papadaki" value="Maria Papadaki" checked="checked">
						  Maria Papadaki
						</label>
						</div>
					  <div class="radio">
						<label for="radios-1">
						  <input type="radio" name="ballot" id="Stavros Shiaeles" value="Stavros Shiaeles">
						  Stavros Shiaeles
						</label>
						</div>
					  <div class="radio">
						<label for="radios-2">
						  <input type="radio" name="ballot" id="radios-2" value="Steve Furnell">
						  Steve Furnell
						</label>
						</div>
					  <div class="radio">
						<label for="radios-3">
						  <input type="radio" name="ballot" id="radios-3" value="No Vote">
						  No Vote
						</label>
						</div>
					  </div>
					</div>
					<br>

					<!-- Button (Double) -->
					<div class="form-group">
					  <label class="col-md-4 control-label" for="button1id"></label>
					  <div class="col-md-8">
						<button id="button1id" name="button1id" class="btn btn-success">Submit Vote</button>
						<button id="button2id" name="button2id" type="button" onclick="location.href='/'" class="btn btn-danger">Cancel Voting</button>
					</div>
					</div>

					</fieldset>
					</form>

				</p>
			</div>
		</div>
		<div class="footer">
			<ul>
				<li>
					<a href="login"><img src="vote.png" alt="Img" /></a>
					<p align="center">
						<a href="login">Cast A Vote</a><br/>
						Return to the front page
					</p>
				</li>
				<li>
					<a href="about"><img src="portfolio.png" alt="Img" /></a>
					<p align="center">
						<a href="about">About Heimdallr</a><br/>
						Learn more about the project
					</p>
				</li>
				<li>
					<a href="contact"><img src="contact.png" alt="Img" /></a>
					<p align="center">
						<a href="contact">Contact</a><br/>
						Details of the project creator
					</p>
				</li>
			</ul>

		</div>
	</div> <!-- /#content -->
</body>
</html>
