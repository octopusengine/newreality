<b>setup:</b> config.ini  
<code>net = <b>single</b> / client / server </code><br/> 
<code>hw = <b>0</b> / 1 </code><br/>
<code>-> <b>default</b></code><br/>

and<br/>
<b>start:</b> start-a123.py<br/><br/><br/>
<hr/>
<hr/>
<h2>3D visualisation</h2>
F1 perspective (A2)<br/>
F2 red&blue stereogr. (A3)<br/>
F3 stereographics (A3)<br/>

<img src="http://www.newreality.eu/wp-content/uploads/2016/08/visual01-600.jpg">


<h2>2D plugins</h2>
1.0.0 > world map<br/>
1.0.0 matrix / noise - next: live game...<br/>
chart / graph<br/>


<h2>3D plugins</h2>
1.0.1 > import cloud points data from <a href=https://github.com/octopusengine/simple3dscanner>github.com/octopusengine/simple3dscanner</a>
stars (testing)<br/>
"3D performance"<br/>

<h2>inputs</h2>
a1 a2 a3 - only standard keyboard and mouse<br/>
b1 - only for Raspbbery Pi3 new interfaces<br/>
<h2>network</h2>
socket <br/>
test? https://docs.python.org/3.5/library/socketserver.html<br/>

<hr />
<h2>config.ini</h2>
<code>//---------------octopus engine config----</code><br />
<br />
<code>ver=1.0.0</code><br />

<code>hw=0</code><br />
<br />

<code>//---------------network------------------</code><br />
<code>net=single</code><br />
<code>//single/server/client</code><br />
<code> </code><br />
<code>ips=1.2.3.5</code><br />
<code> </code><br />
<code>//a - single</code><br />
<code>//b - client-server on one computer  -> ips=localhost</code><br /> 
<code>//c - client-server on two computers -> ips=1.2.3.5 (your server IP)</code><br />
<code> </code><br />
<code>//--------------/network------------------</code><br />

<hr/>
<h2>history</h2>
(A) version serves as a feasibility study<br />
A1 - 0.1 - 2D graphics (testing matrix, movement, idea ..)<br />
A2 - 0.5 - 3D perspective<br />
A3 - 0.9 - 3D stereography for VR + HW test (Raspberry PI3)<br />
-> newreality1.0<br /><br />
(B) next step - nework and cooperation<br />
-> todo 2.0<br /><br />
(C) final? ;-)<br /><br />

<hr/>
