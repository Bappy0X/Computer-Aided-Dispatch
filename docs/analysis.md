[:rewind: Back](/README.md)

# :one: Analysis

- [Problem Definition](#problem-definition)
	- [Before Computers](#before-computers)
	- [Incorporating a Computational Solution](#incorporating-a-computational-solution)
- [Stakeholders](#stakeholders)
- [Research](#research)
- [Features](#features)
	- [Simple Set Up](#simple-set-up)
	- [Day-to-Day Running](#day-to-day-running)
	- [General Maintenance](#general-maintenance)
	- [Architecture Paradigms](#architecture-paradigms)
	- [Maps & Positional Data](#maps--positional-data)
	- [Data Visualisation](#data-visualisation)
	- [Intuitive UI & UX](#intuitive-ui--ux)
	- [User Information & Live Status Tracking](#user-information--live-status-tracking)
- [Limitations](#limitations)
- [Requirements](#requirements)
	- [Development Environment](#development-environment)
	- [Server/Deployment Environment](#serverdeployment-environment)
	- [End User Environment](#end-user-environment)
- [Success Criteria](#success-criteria)

# Problem Definition

The emergency services, delivery services, taxi’s and other private companies all require and rely on “Computer Aided Dispatch” software. This is used to keep track of jobs, track and periodically update records, monitor the workforce and provide better customer service.

These software’s are extremely useful and assist in strategically planning the rotation of resources and assets for a company. This helps to cut down costs and ensure that the workforce is performing as it should, creating rules and tasks on the fly.

CAD (Computer Aided Dispatch) software is also extremely useful for the general public, a client, or customer. Tracking ETA’s of emergency service personnel, deliveries, and taxi’s mean that clients can go by their business, rather than wait.

---

### Before Computers

Pen and paper are extremely inefficient methods of tracking and analysing any process. Requiring excessive amounts of human interaction, pen and paper are more likely to fail.

People can stray on their own path, leading away from protocols and instructions, which within a dispatch environment, are vital they are followed as lives may depend on it.

Ultimately, computers follow a set of explicit instructions, and nothing else - this fundamentally improves the safety and reliability of any dispatch system.

### Incorporating a Computational Solution

1. **Able to directly view workforce performance**
This allows for advanced analytics of your workforce. You're able to ensure that your employees and colleagues are working effectively via graphs and charts.
2. **Decreased costs to the company**
    1. **Server architecture rather than paper and pen**
        1. Clients won't overpay for assets (like paper and pens) that they don't require. Instead, they're able to buy exactly what they need - a server.
        2. There's less human interaction - fundamentally decreasing the rate of failure.
        3. You have an instant access to records - there's no delay or frustration rummaging through physical papers trying to find exactly what you need.
        4. It's easier to archive and back up data, and request it when you need it. This makes reports a lot easier.
    2. **Training**
        1. However, the workforce may need to be retrained in order to use this new system. Whilst some may not have appropriate experience or contact with software, so it may be more difficult to understand.

There are many limitations to using paper and pen. Primarily the costs. Monthly fulfilment of physical goods like pen & paper can be extremely costly, especially when those goods aren't guaranteed to be used. These are also imperishable, where they can only be used for a set time before becoming unusable. Especially paper, where it can only be written and printed and written onto once.

These resources are also difficult to expand. Pen and paper is fundamentally flawed, it's impossible to add more features to them. This restricts the usability of pen and paper significantly.

Computer systems are able to scale horizontally and vertically, infinitely. This means that many more features can be added. Because of this, they're also more affordable and allow for more flexibility.

Online and computational based systems are driven by data. This allows you to have comprehensive insights and analysis into volumes, quality, staff performance and more. This could be daily, or periodical data. This can be represented on the front end by library's such as D3, Highcharts and my favoruite, Zingchart.

However, a computational solution may not be for everyone. Staring at screens causes eye fatigue and strains the eyes of all generations. Whilst older generations might find learning UI difficult. These needs can be filled by improving the friendliness of the user interface.

---

# Stakeholders

There are many key stakeholders for this project and fundamental idea - within many sectors and job roles. This means that expanding and increasing the flexibility of use for the application is a must, in order to supply for all these target markets and demographics

- **The Public Services**
	
	All of the blue light services (police, fire, ambulance) utilise dispatching software to notify emergency personnel to a scene or otherwise act on an incident.
	
	To supply for this stakeholder group, my application must be trustworthy. This means that extreme and rigorous testing is a must - ensuring that my application can be trusted during high intensity situations that this stakeholder group commonly experiences.
    
- **Private Companies**
    - **Taxi-Cabs**
		
		Operating across the globe, many people rely on taxi's in order to commute to and from work, parties, and events.
    	
		These services rely on dispatchers in order to operate efficiently and successfully. A lack of professional and efficient conduct would result in an unhappy customer.
    	
		To appeal to these businesses, the application must display a promising (and real-time) user experience. Each cab driver must understand what they need to do, how to do it and when to do it. Concise and effective user interface is important for this.

    - **Delivery Services**
		
		Civilisation also relies on delivery services to receive online purchases. In recent years, these markets have grew exponentially. Delivery Companies such as Amazon/Prime, Hermes and DHL have seen a massive increase in their market share. This is a great driving force to creating a delivery-friendly application.
    	
		For this, route tracking must be implemented alongside real-time package tracking systems in order to combat the existing market. If the app lacks these features then we may se a decrease in overall business, as these features are desirable to the end-user.

    - **The Gig-based Market**
		
		Lyft and Uber supply services that could also benefit from the use of notifications and tracking. The end-user would be able to track their ride and receive an appropriate ETA. Alike taxi-cab services, this requires a promising and easy to use UI/UX. This also ensures that clients receives happy customers and causes repeat business.
    	
		The application must deliver a great user experience in order to be promised and trusted by private companies. Implementing a free trial or a guest scheme may also be a great incentive to business.

---

# Research

The market for Computer Aided Dispatch is currently dominated by old and outdated software than is proven to be reliable, difficult to use and is expensive. This application must appeal to the aforementioned stakeholders, whilst also developing a unique solution to stand out from the existing market.

Mapping potential competitors on a market matrix will assist in finding a gap within the existing market, and identify unique traits and opportunities for this application. Providing these unique traits and standing out from the market has massive benefits, where sales can be dramatically boosted, and revenue can also be increased. This also allows us to directly compete with existing solutions, boosting market share.

<p align="center"><img src="https://file.coffee/u/TjbUcuHZ16.png" height="400px" alt="Graph illustrating an up-curve between features and price."/></p>
<p align="center">Market matrix displaying the mentioned competitors.</p>

- **OpenCAD**
    
	This is an Open Source solution that runs on the traditional Linux Apache MySQL PHP (LAMP) stack. This may not be a modern solution, but it includes plentiful features - yet still lacking a map. As it's open source, it's free to use, distribute and edit, and can be ran on almost any applicable hardware.

- **Lebanon County Department of Emergency Services**
    
	Under Pennsylvania state ownership, the LC:DES is very public about the services that they offer to the public and emergency services. This information is publicly available to us, so we're able to compare and contrast a real implementation of a potential competitors app within the emergency services.

    This is a very simple solution for dispatchers. A map is integrated within the application, and dispatchers are able to message (and even page/text) different operational units spread throughout the county.

- **Soma Global**
	
	This solution presents itself as a cloud based CAD. It features an online dashboard with integrated maps. Important information is displayed immediately, directly to the user - the end user doesn't have to search in order to find what they need. Addresses, personnel assigned, call status and more information is shown here.

	This service is extremely expandable, where it can be used across multiple devices by many different users. The UI/UX appears simple, and would be easy to adjust to - whilst also maintaining a modernistic feel and look.

	Prices for this solution are not publicly listed, instead you must contact the developers directly. It also appears that the application is hosted for you on remote hardware, and you'll most likely be presented with a monthly charge for this.

- **Dever Software: Dispatch**
    
    Aimed towards private hires like Airport Transfers, Chauffeur Services and more. Clients are able to manage their staff. And end-users will be presented with a user interface that allows them to place orders and create bookings. This gives the client an out-the-box experience that requires no extra setup. This gives the client confidence and allows them to present themselves with professionality.

- **ServiceM8**
    
    This service also presents itself towards private companies and organisations, where job management and organisation is one of its core components and functionalities. It presents the client with a schedule management system and locational/positional data.

    This makes it easier for management to create tasks and schedules for employees. It's charm is to 'eliminate paperwork, improve productivity & provide great service'. This is also relevant to our application, and also what we aim to create.

    This application is purely for task management, but can be used as a dispatching software. Pricing is very flexible, and will allow clients to scale up, or down, depending on what resources we require. This is also something I believe should be implemented with this app. A 14 day free trial is also offered.

This graph illustrates an upcurve. More expensive products utilise more, or more advanced features. There's a wide gap in this market, where move features are less expensive. This is obvious, however, as more features presents an obstacle to companies, organisations or individual, where more work is required to implement it. This may also be time, and in fast paced businesses, time is money.

Using modern technologies and tech stacks may be extremely useful in order to combat this market, as they can be utilised to add more features, quicker and more efficiently, whilst not taking a knock to performance or loss of features, or loss of quality.

---

# Features

The most important attributes of promotion is presenting a product with plentiful features and high quality. This is impossible without an app that isn't feature rich, this means that creating a featureful application is a top priority for this project. This will help to further improve the potential outreach for the application/product.

### Simple Set Up

The user should be instantly interested by the application. It's important that the setup process doesn't turn them away from the application - this would be catastrophic, as the application would never reach an end user, less users would notice its potential, meaning it's more difficult to generate a revenue.

### Day-to-Day Running

The client must be pleased with the application that they're delivered, we'd like to create an application that can promote itself easily. 

### General Maintenance

...Should ideally be kept to a minimum, and should be provided internally, free of cost. Clients should have the best experience possible whilst using this solution - creating brand-loyalty and continue to generate revenue.

### Architecture Paradigms

There are plentiful ways to deploy and serve the application to clients.

- **Source Code & Self-Hosted**
    
    In this process, the source code for the application would be given as a package. In this, we potentially risk security risks, and picking a license for the application would be extremely important to the safety of the application.

    The client would then host the application on their own dedicated server, this may have more setup costs, including time and frustration for engineers, and may prove more difficult to maintain, as different developers may use their own techniques.

- **Shared Hosting**
    
    Here, the owner(s) (myself) would host the code, this prevents the need for external licensing and contains the source-code within internal staff.

    Shared hosting would include multiple instances of the same application running on the same server. Each instance *shares* a portion of resources available on the server.

	To do this, a single VPS instance can be bought (this can be as little as $5 from DigitalOcean) and NGINX can be used in order to proxy and direct traffic from different domains.

- **Dedicated Hosting**
    
    Alike shared hosting, servers and code would be hosted under one owner.

    Dedicated Hosting entails one dedicated server per Instance, this can be more costly, however can prove cost-effective for bigger and larger scaled apps, and higher user demand.

    See, when more users are active on an application, that application requires more active resources in order to function properly - as resource requirements will increase over each request. If the application doesn't have access to enough resources, the service will hang and appear slow to the end user. Using dedicated hosting will avoid this - until the application reaches a certain scale, at which load-balancing is required between multiple dedicated servers.

Shared hosting and dedicated hosting and the best to choose in this instance, as they're more rapidly scalable, require less maintenance from the end-user, and are on-site, so the application is more easily manageable. This centralised infrastructure will prove massively beneficial to the end user.

**Privacy**

Users of Big-Tech companies are often scared of their data being breached or misused. Engaging in our clients trust is extremely important to the success of the application.

We must comply with GDPR regulation, as I (the current owner of the application) live in the UK, and must abide by UK law.

### Maps & Positional Data

To create a USP (Unique Selling Point), the application can utilise a feature that allows tracking of positional data, pinpointed onto a map. We can use pre-existing libraries in order to minimise development times. This also means developers won't have to worry about specifics, providing a reputable and 'good' solution is used.

- **GMaps**

    We're able to generate maps using Google Maps, a popular pinpointed app. Pinpoints, lines and menus can be created. This appears to be the most basic solution, and doesn't allow for much expandability.
    
- **jHere**
    
    This is used by many larger scale companies, such as Amazon. It uses a custom, home-grown map, known as 'HERE' and is interactive using jQuery. This is also a basic solution, however it appears much more modern and allows for more expandability.

- **D3**
    
    This is a massively powerful tool that has many different uses. We're able to generate maps and render advanced graphics. A great example of this can be seen [here](http://d3.artzub.com/wbca/).

- **Leaflet**
    
    ...Is a light-weight map engine. You're able to use it to draw custom maps and other diagrams. Other functionality be added on by using different addons and plugins.

### Data Visualisation

It's extremely useful to view in-depth analytics about their workforce and different situations. Within the emergency services, response times are extremely important are critical to the element of success. Using graphs and data visualisation techniques, response times can be increased by assigning the most appropriate units to calls and situations.

### Intuitive UI & UX

I was once told: 'User Interface is like a joke; if you must explain it, then it’s bad'. Whilst developing this application I should keep this in mind. This will help to ensure that the application will be more complete and ready for the end-user.

Ideally, we don't want to have to create an in-depth tutorial for the end-user. This is slow and confuse some. This would also mean that our application is not suitable, as it's not intuitive. The user should be able to learn through play, and the interface should be easy to learn - regardless of their prior experience. This will help to decrease training costs and ease the minds of clients.

This would also help to decrease our costs as we'd require less support staff, so more time can be spend innovating and running the project.

### User Information & Live Status Tracking

Clients will often want to keep track of assets in real-time. This is an important aspect of dispatch operations and contributes to the minimisation of costs and extensive service. This also helps to develop a brand's image, as more clients can be reaches and be served.

---

# Limitations

- **Abiding by Time**

	Developing high-quality features takes time. Ideally, this application should be ready to release ASAP in order to combat the market the best it possibly can, before more competitors arise and current competitors become aware of their weaknesses.

    The application should be released in a fully functional state, and should be iteratively tested to ensure its feature-set is fully functional. However, this costs lots of time - lots of it. We're already trimming the amount of time required by using pre-built libraries to interact with our app.

    Decreasing the time-to-market and overall lead time is a fundamental requirement to a healthy release with this app. We want to be able to combat the existing competitors, and dominate the open gap within the market.

    Releasing a fully-functional app will secure a place within the industry 

- **Financial Restriction**

	This application doesn't cost much to produce, thanks in par with the usage of different libraries. This application is intended to be developed without a necessary investment. This means that specialised staff (like graphics designers) will not be hired, and additional staff/developers will, also, not be hired.

    When deploying the solution, a centralised server will need to be used. As mentioned before, the application can be deployed on a VPS. DigitalOcean offers this product for as little as $5. And may also be free from services such as Heroku.

- **Skillset Restrictions**

    I currently hold a very vast skillset. I am proficient in knowhow for all of the technologies mentioned within this documentation. I currently hold professional experience working on many different technology stacks.

    However, I *always* like a challenge. This will be mentioned more within the Design documentation.


---

# Requirements

### Development Environment

<table>
	<thead>
		<tr>
			<th colspan="2">Visual Studio Code</th>
		</tr>
		<tr>
			<th>Requirement</th>
			<th>Justification</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<ul>
					<li>1.6GHz or faster processor</li>
					<li>1GB of RAM</li>
					<li>SSD > 200mb</li>
					<li>
						<strong>Operating System:</strong><br>
						<ul>
							<li>OS X Yosemite</li>
							<li>Windows 7 (with .NET Framework 4.5.2), 8.0, 8.1 or 10 (32-bit and 64-bit)</li>
							<li>Linux (Debian): Ubuntu Desktop 14.04, Debian 7</li>
							<li>Linux (Red Hat): Red Hat Enterprise Linux 7, CentOS 7, Fedora 23</li>
						</ul>
					</li>
				</ul>
			</td>
			<td>In order to write and develop code for this application, Visual Studio Code will be used. This will create a very usable work environment. I would recommend an SSD to allow for faster loading times.</td>
		</tr>
	</tbody>
</table>

<table>
	<thead>
		<tr>
			<th colspan="2">Python 3.8.2 Runtime Environment</th>
		</tr>
		<tr>
			<th>Requirement</th>
			<th>Justification</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<ul>
					<li>Multi-Core 2GHz or faster CPU</li>
					<li>2 GB of RAM</li>
				</ul>
			</td>
			<td>In order to serve our application on a localhost (for our developer), we should have a fast processor and plentiful RAM. This will allow for python files to be kept within RAM and pages to be templated and produced faster.</td>
		</tr>
	</tbody>
</table>

### Server/Deployment Environment

<table>
	<thead>
		<tr>
			<th colspan="2">Python 3.8.2 Server-Side Runtime Environment</th>
		</tr>
		<tr>
			<th>Requirement</th>
			<th>Justification</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
				<ul>
					<li>1 CPU</li>
					<li>25GB SSD</li>
					<li>1 GB of RAM</li>
					<li>1TB Transfer</li>
					<li>Linux Ubuntu (LTS) Bionic 18.04 x64 (No desktop environment, purely CLI)</li>
				</ul>
			</td>
			<td>Having a powerful server machine will allow us to serve as many end users as possible, as pages will spend less time within the processing phase – the same applies with an SSD, files can be fetched and utilised faster.<br><br>Thanks to the less taxing OS we are also able to have a smaller amount of RAM.<br><br>With a server machine, it’s important that we have a high amount of available transfer.<br><br>We can also use a scalable SaaS – e.g., DigitalOcean or Scaleway. This will allow us to scale up our application if we receive an increased amount of traffic.</td>
		</tr>
	</tbody>
</table>

### End User Environment

The only requirement for the end user will be to install a browser and use a device that can access the internet. One objective for this application will be to produce an accessible and responsive user interface, that allows the application to reach more potential clients.

---

# Success Criteria

In order to measure my success in the development and production of this application, a success criteria will be set. This will create an end-goal - a physical boundary of success.

<table>
	<thead>
		<tr>
			<th>Criteria</th>
			<th>Description/Notes</th>
			<th>Methodology of Measurement</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th>Create a usable UI and functional UX.</th>
			<td>This must be measured both during the development process, and prior to release. Stakeholders must be able to enjoy the experience that they receive - and this will be measured with a user survey.</td>
			<td>This will either be displayed on the site in a "please give feedback" fashion, or by a post-testing survey. In order to succeed, a minimum rating of 8/10 should be given. However, anything below 10 indicates a lack of success, so it should be worked on.</td>
		</tr>
		<tr>
			<th>Require minimal training (relating to above)</th>
			<td>In order to attract as many potential clients for this application as possible, the training process must either be minimal, or non-existant for this application. This will help to drive down costs and resources that could be better spent elsewhere - this includes time, which is very valuable for businesses.</td>
			<td>Prior to the alpha-testing process, each user will explain how they found the User Experience.</td>
		</tr>
		<tr>
			<th>Incorporate a Responsive UI that will function perfectly on all devices.</th>
			<td>The application should be able to be used on any mobile device, including phones, tablets, laptops and more, whilst also remaining usable and powerful on desktop. This may be important to remember when picking and using libraries, as some can be resource intensive.</td>
			<td>During development, and after final release, both virtual and physical devices can be utilised to test the application. To be successful, the application must scale well across all devices, and all features (regardless of any advanced capabilities) should be usable.</td>
		</tr>
		<tr>
			<th>Boast a unique feature-set unlike any competitor.</th>
			<td>To compete with cometitors within this market, this application must be able to utilise a unique toolbelt of tools and features. This will create a Unique Selling Point for this application, and will be important when creating keen and interested clients.</td>
			<td>When the application is fully developed and prepped for initial release, the features-set should be compared to a selection of apps developed and released by/from competitors. This can be done in a table, and the effectiveness of these features can be measured in a user survey.</td>
		</tr>
		<tr>
			<th>Be released free-of-cost.</th>
			<td>To comply with the restriction of a zero-budget, this application should be developed and released free of charge. This means that nobody can be hired, or assist with the development process. This also assists with keeping the application 100% mine. (Prior to completion of the project, this will be released as source code under an open source license. The intention of this is to help others with the A-Level Computer Science Assessment, of year 2021, as well as assist those that may be developing a similar application)</td>
			<td>Simply put, nothing should be spent on this project, and nobody should've actively contributed within the development process. Contributers will be allowed to contribute prior to completion and I'll actively allow and support this. After all, my code, and my solution, will not be perfect - there will always be room for potential improvement.</td>
		</tr>
		<tr>
			<th>Fit the use-case of a wide range of stakeholders.</th>
			<td>In order to compete with as many products as possible, and create a wide user/client-base, this product should be suitable for a wide range of clients, this includes both private and public services, globally, worldwide. It should also accomplish this without straying away from the inital objective - creating a CAD/Dispatch software.</td>
			<td>Stakeholders should be invited equally, and should be mapped on a line graph. This graph will then display the amount of those those that support, enjoy or endorse the application.</td>
		</tr>
		<tr>
			<th>Be deployed in a timely and easy manner.</th>
			<td>The application must be able to be deployed by a client quickly.</td>
			<td>This will require both a time measurement showing the beginning-to-end timedelta and personal measurement (1-10), representing the client's satisfaction with the deployment process.</td>
		</tr>
	</tbody>
</table>

---

### Joshua Vaughan
