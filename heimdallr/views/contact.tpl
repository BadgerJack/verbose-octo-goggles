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
					<div id="contact_form">
                        <form method="post" name="contact" action="contact.php">
                            <div class="col_175 left">
                                <label for="author">Name:</label> <input type="text" id="author" name="author" class="required input_field" />
                            </div>
                            <div class="col_175 right">
                                <label for="email">Email:</label> <input type="text" id="email" name="email" class="validate-email required input_field" />
                            </div>

                            <label for="text">Message:</label> <textarea id="text" name="text" rows="0" cols="0" class="required"></textarea>
                            <input type="submit" value="Send" id="submit" name="submit" class="submit_btn left" />
							<input type="reset" value="Reset" id="reset" name="reset" class="submit_btn right" />
                        </form>
                </div>
                <br>
								<p>Project Heimdallr was created by Jack Tolley, as part of his final project <br> on the BSc Computer & Information Security degree at Plymouth University.</p>
                <br>
								<p>If you'd like to get in touch, send a message using the contact form <br> to the right, or find me online using one of the below links.</p>
                <br>
                <p>Feedback is always appreciated, and I'd love to hear any suggestions.</p>
                <br>
                <br>
                <div>&nbsp;&nbsp;&nbsp;&nbsp;
									<a href="https://plus.google.com/u/1/105022475803420128947"><img src="google-64x64.png"></a>&nbsp;&nbsp;&nbsp;&nbsp;
                	<a href="https://www.linkedin.com/in/badgerjack/"><img src="linkedin-64x64.png"></a>&nbsp;&nbsp;&nbsp;&nbsp;
                	<a href="https://www.youtube.com/channel/UCTuLlYEo1s0i5UhHvArWKGQ"><img src="youtube-64x64.png"></a>&nbsp;&nbsp;&nbsp;&nbsp;
									<a href="https://twitter.com/OptimusTheorem"><img src="twitter-64x64.png"></a>&nbsp;&nbsp;&nbsp;&nbsp;
                </div>
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
