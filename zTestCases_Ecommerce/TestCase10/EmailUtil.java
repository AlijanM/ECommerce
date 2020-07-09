//********************************************************************************************
//*    Guru99 eCommerce Live Project    
//*    Participant : Krishna Rungta                    
//*                                                                                                                                                          *
//********************************************************************************************
/* Test Case requirements/descriptions:
 *    Export all Orders in csv file and display these information in console and 
 *    you are able to send this file to another email id as attachment 
 * Note: Access to backend of the site. UserId "user01" and pw "user001"
 *    
1. Go to http://live.demoguru99.com/index.php/backendlogin
2. Login the credentials provided
3. Go to Sales-> Orders menu
4. Select 'CSV' in Export To dropdown and click Export button.
5. Read downloaded file and display all order information in console windows
6. Attach this exported file and email to another email id

Expected results:
1) Console displays all order information
2) Email is sent successfully
*/

	package eCommerceLive;
	import javax.activation.DataHandler;
    import javax.activation.DataSource;
    import javax.activation.FileDataSource;
    import javax.mail.*;
    import javax.mail.internet.*;
    import java.util.*;

	public class EmailUtil {
		
		  private static final String SMTP_HOST_NAME = "smtp.gmail.com";
	      private static final String SMTP_AUTH_USER = "userid";
	      private static final String SMTP_AUTH_PWD  = "pass";
	      
	      private static final String emailMsgTxt      = "Orders List in CSV formatted file";
	      private static final String emailSubjectTxt  = "Orders List in CSV formatted file";
	      private static final String emailFromAddress = "userid@gmail.com";

	      // Add List of Email address to who email needs to be sent to
	      private static final String[] emailList = {"supportw11@axyz.com", "BMX97M@tpg.com"};
	      private static String sFilename = null;
	      
		 
	 public static void emailUtil(String vFilename) throws MessagingException
	      {

	      // 6. Attach this exported file and email to another email id
    	      sFilename = vFilename;
	    	  EmailUtil smtpMailSender = new EmailUtil();
	    	  smtpMailSender.postMail( emailList, emailSubjectTxt, emailMsgTxt, emailFromAddress);
	    	  
	      }

      private BodyPart messageBodyPart;

      public void postMail( String recipients[ ], String subject,
                                String message , String from) throws MessagingException
      {
        //boolean debug = false;
        //Set the host smtp address 
         Properties props = new Properties();
         props.put("mail.smtp.host", SMTP_HOST_NAME);
         props.put("mail.smtp.auth", "true");

        Authenticator auth = new SMTPAuthenticator();
        Session session = Session.getDefaultInstance(props, auth);
        // session.setDebug(debug);
       
        // create a message
        Message msg = new MimeMessage(session);
        
        // set the from and to address
        InternetAddress addressFrom = new InternetAddress(from);
        msg.setFrom(addressFrom);
          
        // new code added
        Multipart multipart = new MimeMultipart();
        // multipart.addBodyPart(messageBodyPart);
       
        // Part two is attachment
        messageBodyPart = new MimeBodyPart();
        String filename = sFilename;
        DataSource source = new FileDataSource(filename);
        messageBodyPart.setDataHandler(new DataHandler(source));
        
        messageBodyPart.setFileName(sFilename);
        messageBodyPart.setDescription(message);
        multipart.addBodyPart(messageBodyPart);
       
        // Put parts in message
        msg.setContent(multipart);
       
        InternetAddress[] addressTo = new InternetAddress[recipients.length];
        for (int i = 0; i < recipients.length; i++)
        {
            addressTo[i] = new InternetAddress(recipients[i]);
        }
        
        msg.setRecipients(Message.RecipientType.TO, addressTo); 
        
      // Setting the Subject and Content Type
        msg.setSubject(subject);
        msg.setContent(multipart);
        Transport.send(msg);
          
     }

    /**
    * SimpleAuthenticator is used to do simple authentication
    * when the SMTP server requires it.
    */
    private class SMTPAuthenticator extends javax.mail.Authenticator
    {

        public PasswordAuthentication getPasswordAuthentication()
        {
            String username = SMTP_AUTH_USER;
            String password = SMTP_AUTH_PWD;
            return new PasswordAuthentication(username, password);
        }
    }

 }
  
	  
	
