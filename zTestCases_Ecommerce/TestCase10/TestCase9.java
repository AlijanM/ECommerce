//********************************************************************************************
//*    Guru99 eCommerce Live Project    
//*    Participant : Krishna Rungta                    
//*                                                                                                                                                       *
//********************************************************************************************
/*  Verify Discount Coupon works correctly
 *
Test Case Description:
1. Go to http://live.demoguru99.com/
2. Go to Mobile and add IPHONE to cart
3. Enter Coupon Code
4. Verify the discount generated

TestData:  Coupon Code: GURU50
Expected result:
1) Price is discounted by 5%

*/

package eCommerceLive;

import static org.junit.Assert.assertEquals;

import org.testng.annotations.AfterTest;
import org.testng.annotations.Test;
import org.testng.annotations.BeforeTest;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class TestCase9 {
	  private WebDriver driver;
	  private String baseUrl;
	  public double GURU50 = 0.05;
	  
	  
	@BeforeTest
	public void setUp() throws Exception {
		driver = new FirefoxDriver();
	    baseUrl = "http://live.demoguru99.com/";
	    //driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
	    driver.get("http://live.demoguru99.com/");
	  }
	  
	  @Test
	  public void testTestCase9() throws Exception {
		  // Step 1. Go to http://live.demoguru99.com                                         
		   
		    
		 // 2a. Go to Mobile 
		    driver.findElement(By.linkText("MOBILE")).click();
		    
		 // switching to new window                                                    
		    for (String handle : driver.getWindowHandles()) {
		    	driver.switchTo().window(handle);
		    	}
		    Thread.sleep(2000); 
		    
		    // 2b. and add IPHONE to cart
		    driver.findElement(By.xpath(".//*[@id='top']/body/div[1]/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[3]/div/div[3]/button")).click();
		    
		    for (String handle : driver.getWindowHandles()) {
		    	driver.switchTo().window(handle);
		    	}
		    Thread.sleep(2000);
		   
		    driver.findElement(By.id("coupon_code")).clear();
		    driver.findElement(By.id("coupon_code")).sendKeys("GURU50");
		   
		    driver.findElement(By.xpath("//button[@title='Apply']")).click();
		    
		    // this is the Sub Total amount displayed (e.g. $500.00)
		    String vSubTot = driver.findElement(By.xpath(".//*[@id='shopping-cart-totals-table']/tbody/tr[1]/td[2]/span")).getText().trim(); 
		    
		    // this is the discount amount displayed (e.g. $50.00)
		    String vDiscDisp = driver.findElement(By.xpath(".//*[@id='shopping-cart-totals-table']/tbody/tr[2]/td[2]/span")).getText().trim();
		    
		    // this is the Generated discount amount displayed (e.g. $475.00)
		    String vDiscountedAmtDisplayed = driver.findElement(By.xpath(".//*[@id='shopping-cart-totals-table']/tfoot/tr/td[2]/strong/span")).getText().trim();
		    		    
		    // Remove the $ sign 
		    String sSubTot = vSubTot.replaceAll("\\$", " ");                // e.g. $500.00	        
	        String sDiscDisp = vDiscDisp.replaceAll("\\$", " ");            // e.g. $25.00	        
	        String sDiscountedAmtDisplayed = vDiscountedAmtDisplayed.replaceAll("\\$", " "); 
	        
	        // Remove the - negative sign
	        String sNegDisc = sDiscDisp.replaceAll("\\-", " ");              // e.g. -25.00
	        
	        // trim the String variables to get it ready for calculation
	        String fSubTot = sSubTot.trim();                                 // e.g. $500.00	        
	        String fDiscDisp = sNegDisc.trim();                              // e.g. $25.00	        
	        String fDiscountedAmtDisplayed = sDiscountedAmtDisplayed.trim(); // e.g. $475.00
	        
		    // ***************************************************************************************************************************
		    // discount amount calculations and comparisons between the derived amount against the discount amount displayed on the page
		    // ***************************************************************************************************************************		    
		    
		    double dSubTot = Double.parseDouble(fSubTot);                                 // e.g.        $500.00
		    double dDiscDisp = Double.parseDouble(fDiscDisp);                             // e.g.         $25.00
		    double dDiscountedAmtDisplayed = Double.parseDouble(fDiscountedAmtDisplayed); // e.g.        $475.00
		    
		    // multiply the dSubTot by the GURU50 discount rate (GURU50 = 5% = 0.05) 
		    double discountedAmt = (dSubTot * GURU50);     // discountedAmt is the calculated discounted amount (e.g. $25.00)	
		    double dDiscPrice = (dSubTot - discountedAmt); // e.g. Discounted Price (e.g. $475) = Sub Total ($500.00) less the 5% discount amount ($25.00)
		    
		    // ************************************************************************************************
		    //   compare & assert that the displayed discount amount is equal to the derived discount amount
		    // ************************************************************************************************
		    // the amount of discount (e.g. $25.00 = $500 * 5%) compared to the amount of discount as displayed on the page (e.g. $25)
		    if (discountedAmt == dDiscDisp){
		    		System.out.println("*** Derived discount amount   = " + discountedAmt);
		    		System.out.println("*** Displayed discount amount = " + dDiscDisp);
		    }else
		      { System.out.println("*** Derived discount amount not equal displayed discount amount ***");
		    }	
		    
		    String string_discountedAmt = Double.toString(discountedAmt);
		    String string_dDiscDisp = Double.toString(dDiscDisp);
		    try {
		        assertEquals(string_discountedAmt, string_dDiscDisp);
		      } catch (Error e) {
		    	  System.out.println("*** Derived discount amount not equal displayed discount amount ***");
		    	  e.printStackTrace();	
		      }
		 
		    // **************************************************************************************************************************************
		    // compare & assert that the displayed discounted price is equal to the derived discounted price
		    // derived discounted price (e.g. $475.00 = $500 less $25)) compared to the displayed discounted price ($475.00) as displayed on the page
		    // **************************************************************************************************************************************
		    if (dDiscPrice == dDiscountedAmtDisplayed){
	    		System.out.println("*** Derived discounted price   = " + dDiscPrice);
	    		System.out.println("*** Displayed discounted price = " + dDiscountedAmtDisplayed);
		    }else
		    	{ System.out.println("*** Derived discounted price not equal displayed discounted price ***");
		    }	
		    
		    String string_dDiscPrice = Double.toString(dDiscPrice);
		    String string_discountedAmtDisplayed = Double.toString(dDiscountedAmtDisplayed);
		    try {
		        assertEquals(string_dDiscPrice, string_discountedAmtDisplayed);
		      } catch (Error e) {
		    	  System.out.println("*** Derived discount amount not equal displayed discount amount ***");
		    	  e.printStackTrace();	
		      }
	  }
	
	@AfterTest
	public void tearDown() throws Exception {
		Thread.sleep(3000);
		//driver.quit();
	  }
	}
