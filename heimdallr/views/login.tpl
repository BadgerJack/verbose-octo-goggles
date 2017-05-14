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
				<fieldset>
					<p><b>Welcome to the Heimdallr voting platform</b></p>
					<br>
					<p>Today, we are voting on who is our favourite lecturer.</p>
					<br>
					<p>Your voter ID is automatically generated here, but would usually be entered along with
					 confirmation of your details. This would act as user authentication, in association with
					 the national voter database.</p>
					<br>

					<form class="form-horizontal" action="/login" method="post">
						<div>
							<input name="voterID" type="text" placeholder="Voter ID" value = "{{randnum}}" required="" readonly>
							<label class="col-md-4 control-label" for="Name">(Required)</label>
						</div>

						<div>
							<input name="email" type="text" placeholder="User Email">
						</div>
						<br>
						<div class="col-md-8">
							<button id="button1id" name="button1id" class="btn btn-success">Continue</button>
					  </div>
					</form>
					<br>
					<p>A user guide for this website is available <a href="docs/userguide_data.html#using-the-website">here</a>.</p>
				</fieldset>
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
