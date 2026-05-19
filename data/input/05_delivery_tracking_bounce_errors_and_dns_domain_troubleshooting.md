# Delivery tracking, bounce errors and DNS/domain troubleshooting

This file is retrieval-facing content for vector-store ingestion. The answers have been cleaned to remove copied or generic case-description text, TOC/index artifacts, repeated response boilerplate, and noisy separators.

## How do I check incoming mail logs when a user is not receiving emails from a sender?

ID: `how_do_i_check_incoming_mail_logs_when_a_user_is_not_receiving_emails_from_a_sender`
Category: Admin Panel
Subcategory: Mail Delivery Report
Source section: Scenario 1 – Incoming: User Is Not Receiving Emails From a Specific Sender

Alternate questions:
- How can I check incoming mail logs when a user is not receiving emails from a sender?

Answer:
- Scenario1 – Incoming: User Is Not Receiving Emails From a Specific Sender A user reports that they are not receiving emails from a specific sender email address or domain. Using the Mail Delivery Report, the administrator can verify whether the emails were: - Received by the server - Blocked by filtering policies - Delivered successfully - Rejected or bounced Steps to Check Email Delivery Logs:

Keywords: check, incoming, logs, not, receiving, emails, sender, delivery

---

## How to block spam emails?

ID: `how_to_block_spam_emails`
Category: Webmail
Subcategory: Spam Handling
Source section: How to block spam emails?

Alternate questions:
- How do I block spam emails?
- How can I block spam emails?

Answer:
If you receive a spam email in your Inbox, you can report and block it using the steps below: Steps to Report Spam (User Level): - Open the Email - Click on “Report Spam” (Below the Subject Line of the email) - The sender will be added to your block sender list Step 2: Share Email Headers: - Open the email - Click on “Show Full Headers” - Copy the complete headers Step 3: Download Email File: - Click on the 3 dots (⋮) menu after opening the spam email - Select “Download mail in EML format” Step 4: Share with Support: - Send headers + EML file to support@rediffenterprisepro.com Notes: - Reporting spam blocks the sender for your account - Header and eml analysis helps identify the source and improve spam filtering - Support team can block similar spam patterns at server level

Keywords: block, spam, emails, handling

---

## You cannot send mails from this domain. Kindly contact customer support

ID: `you_cannot_send_mails_from_this_domain_kindly_contact_customer_support`
Category: Webmail
Subcategory: How To
Source section: You cannot send mails from this domain. Kindly contact customer support

Alternate questions:
- How do I you cannot send mails from this domain. kindly contact customer support?
- How can I you cannot send mails from this domain. kindly contact customer support?

Answer:
This SOP explains the error message “You cannot send emails from this domain. Kindly contact customer support”, which appears when a user attempts to send an email from a domain that is not properly configured or has been recently configured with the required Rediff MX records in the domain DNS. -

Keywords: cannot, send, kindly, contact, customer, support

---

## Your email could not be sent at this time. Please contact the administrator

ID: `your_email_could_not_be_sent_at_this_time_please_contact_the_administrator`
Category: Webmail
Subcategory: How To
Source section: Your email could not be sent at this time. Please contact the administrator

Alternate questions:
- How do I your email could not be sent at this time. please contact the administrator?
- How can I your email could not be sent at this time. please contact the administrator?

Answer:
This SOP explains the error message “Your email could not be sent at this time. Please contact the administrator”, which appears when a user attempts to send an email but the email account has been temporarily blocked by the abuse team due to spam activity, or when the domain is in suspension mode. -

Keywords: could, not, sent, time, contact, administrator

---

## 553 sorry, your envelope sender is in my badmailfrom list (#5.7.1). REF-ID : MBFD

ID: `553_sorry_your_envelope_sender_is_in_my_badmailfrom_list_5_7_1_ref_id_mbfd`
Category: Bounce
Subcategory: How To
Source section: 553 sorry, your envelope sender is in my badmailfrom list (#5.7.1). REF-ID : MBFD

Alternate questions:
- How do I 553 sorry, your envelope sender is in my badmailfrom list (#5.7.1). ref-id : mbfd?
- How can I 553 sorry, your envelope sender is in my badmailfrom list (#5.7.1). ref-id : mbfd?
- Why am I seeing 553 sorry, your envelope sender is in my badmailfrom list (#5.7.1). REF-ID : MBFD?

Answer:
This SOP explains the bounce error “553 sorry, your envelope sender is in my badmailfrom list (#5.7.1). REF-ID: MBFD”, which occurs when emails sent from a particular sender to Rediffmail Enterprise User are rejected due to spam-filtering restrictions. This issue may occur in either of the following scenarios: - The sender’s domain is blacklisted by the spam filtering service surbl.org, or The recipient, using Rediffmail Enterprise email services, has manually blocked the sender’s email address through the Block/Unblock Sender option. -

Keywords: sorry, envelope, sender, badmailfrom, list, ref-id, mbfd, bounce

---

## 554 Domain used for Authentication is different than the sender's Domain (#5.7.1)

ID: `554_domain_used_for_authentication_is_different_than_the_sender_s_domain_5_7_1`
Category: Bounce
Subcategory: How To
Source section: 554 Domain used for Authentication is different than the sender's Domain (#5.7.1)

Alternate questions:
- How do I 554 domain used for authentication is different than the sender's domain (#5.7.1)?
- How can I 554 domain used for authentication is different than the sender's domain (#5.7.1)?
- Why am I seeing 554 Domain used for Authentication is different than the sender's Domain (#5.7.1)?

Answer:
This SOP explains the bounce error “554 Domain used for Authentication is different than the sender's Domain (#5.7.1)”, which occurs when the authenticated user (username) does not match the sender’s email address while sending emails through an email client / Mail Application. -

Keywords: used, authentication, different, sender, bounce

---

## 554 Suspicious virus code detected, message not accepted (#5.7.7)

ID: `554_suspicious_virus_code_detected_message_not_accepted_5_7_7`
Category: Bounce
Subcategory: How To
Source section: 554 Suspicious virus code detected, message not accepted (#5.7.7)

Alternate questions:
- How do I 554 suspicious virus code detected, message not accepted (#5.7.7)?
- How can I 554 suspicious virus code detected, message not accepted (#5.7.7)?
- Why am I seeing 554 Suspicious virus code detected, message not accepted (#5.7.7)?

Answer:
This SOP explains the bounce error “554 Suspicious virus code detected, message not accepted (#5.7.7)”, which occurs when the Rediff system detects virus or malicious content in the email being sent. -

Keywords: suspicious, virus, code, detected, not, accepted, bounce

---

## Can multiple MX/SPF/DKIM records cause issues?

ID: `can_multiple_mx_spf_dkim_records_cause_issues`
Category: DNS
Subcategory: FAQ
Source section: Common FAQ: DNS Records Not Pointing Properly

Alternate questions:
- How do I can multiple mx/spf/dkim records cause issues?
- How can I can multiple mx/spf/dkim records cause issues?

Answer:
Yes. - Multiple MX records pointing to different providers → email delivery failures - Multiple SPF records → SPF validation fails - Incorrect DKIM selectors → authentication fails

Keywords: multiple, spf, dkim, records, cause, issues, dns, faq

---

## CNAME_lookup_failed_temporarily._(#4.4.3)

ID: `cname_lookup_failed_temporarily_4_4_3`
Category: Bounce
Subcategory: How To
Source section: CNAME_lookup_failed_temporarily._(#4.4.3)

Alternate questions:
- How do I cname_lookup_failed_temporarily._(#4.4.3)?
- How can I cname_lookup_failed_temporarily._(#4.4.3)?
- Why am I seeing CNAME_lookup_failed_temporarily._(#4.4.3)?

Answer:
This SOP explains the bounce error “CNAME_lookup_failed_temporarily._(#4.4.3)”, which occurs when the sender mail server is unable to locate the required MX record and attempts to deliver the email using a CNAME host instead. -

Keywords: cname_lookup_failed_temporarily, bounce

---

## From: Mail Delivery System Mailer-Daemon@Sophos abdd@test.com all hosts for 'test.com' have been failing for a long time (and retry time not reached)

ID: `from_mail_delivery_system_mailer_daemon_sophos_abdd_test_com_all_hosts_for_test_com_have_b`
Category: Bounce
Subcategory: How To
Source section: From: Mail Delivery System Mailer-Daemon@Sophos abdd@test.com all hosts for 'test.com' have been failing for a long time (and retry time not reached)

Alternate questions:
- How do I from: mail delivery system mailer-daemon@sophos abdd@test.com all hosts for 'test.com' have been failing for a long time (and retry time not reached)?
- How can I from: mail delivery system mailer-daemon@sophos abdd@test.com all hosts for 'test.com' have been failing for a long time (and retry time not reached)?

Answer:
This SOP explains the bounce error “From: Mail Delivery System Mailer-Daemon@Sophos abdd@test.com all hosts for 'test.com' have been failing for a long time (and retry time not reached)”, which occurs when emails cannot be delivered due to prolonged delivery delays at the recipient side. -

Keywords: delivery, system, mailer-daemon, sophos, abdd, test, com, hosts, have, been, failing, long

---

## How can I verify my DNS records?

ID: `how_can_i_verify_my_dns_records`
Category: DNS
Subcategory: FAQ
Source section: Common FAQ: DNS Records Not Pointing Properly

Alternate questions:
- How do I verify my dns records?

Answer:
You can verify DNS records using: - Online tools (MXToolbox, DNS Checker, etc.) - Your domain registrar’s DNS panel

Keywords: verify, dns, records, faq

---

## How do I check outgoing mail logs when a user sent an email but the recipient did not receive it?

ID: `how_do_i_check_outgoing_mail_logs_when_a_user_sent_an_email_but_the_recipient_did_not_rece`
Category: Admin Panel
Subcategory: Mail Delivery Report
Source section: Scenario 2 - Outgoing: User Has Sent the Email but the Recipient Has Not Received It

Alternate questions:
- How can I check outgoing mail logs when a user sent an email but the recipient did not receive it?

Answer:
Scenario 2 - Outgoing: User Has Sent the Email but the Recipient Has Not Received It A user reports that they have successfully sent an email, however the recipient has not received the message. Using the Mail Delivery Report, the administrator can verify whether: - The email was successfully sent from the user mailbox - The recipient mail server accepted the message - The email was rejected or bounced - The delivery was completed at the recipient MX server level

Keywords: check, outgoing, logs, sent, but, recipient, did, not, receive, delivery

---

## How do I use Mail Delivery Report to trace incoming and outgoing email delivery?

ID: `how_do_i_use_mail_delivery_report_to_trace_incoming_and_outgoing_email_delivery`
Category: Admin Panel
Subcategory: Mail Delivery Report
Source section: MAIL DELIVERY REPORT

Alternate questions:
- How can I use mail delivery report to trace incoming and outgoing email delivery?

Answer:
- MAIL DELIVERY REPORT This SOP explains the Mail Delivery Report feature available in Rediffmail Enterprise email services, which allows administrators to trace logs of incoming and outgoing emails. Using this feature, administrators can track email delivery status, identify delivery failures, analyze bounce reasons, and verify whether emails were successfully sent or received. -

Keywords: use, delivery, trace, incoming, outgoing

---

## How long do DNS changes take to apply?

ID: `how_long_do_dns_changes_take_to_apply`
Category: DNS
Subcategory: FAQ
Source section: Common FAQ: DNS Records Not Pointing Properly

Alternate questions:
- How do I how long do dns changes take to apply?
- How can I how long do dns changes take to apply?

Answer:
DNS changes typically take: - 5 minutes to 4 hours in most cases - Up to 24–48 hours globally (due to DNS propagation) During this time, email or website behaviour may be inconsistent.

Keywords: long, dns, changes, take, apply, faq

---

## MailBox not found Remote Host said 550 “the mail server detected your message as spam and prevented delivery”

ID: `mailbox_not_found_remote_host_said_550_the_mail_server_detected_your_message_as_spam_and_p`
Category: Bounce
Subcategory: How To
Source section: MailBox not found Remote Host said 550 “the mail server detected your message as spam and prevented delivery”

Alternate questions:
- How do I mailbox not found remote host said 550 “the mail server detected your message as spam and prevented delivery”?
- How can I mailbox not found remote host said 550 “the mail server detected your message as spam and prevented delivery”?

Answer:
This SOP explains the bounce error “MailBox not found Remote Host said 550 ‘the mail server detected your message as spam and prevented delivery’”, which occurs when the recipient mail server classifies the email as spam and blocks delivery. -

Keywords: mailbox, not, found, remote, host, said, server, detected, spam, prevented, delivery, bounce

---

## MailBox not found Remote host said: 550 5.7.0 message rejected per spf policy ?

ID: `mailbox_not_found_remote_host_said_550_5_7_0_message_rejected_per_spf_policy`
Category: Bounce
Subcategory: How To
Source section: MailBox not found Remote host said: 550 5.7.0 message rejected per spf policy ?

Alternate questions:
- How do I mailbox not found remote host said: 550 5.7.0 message rejected per spf policy?
- How can I mailbox not found remote host said: 550 5.7.0 message rejected per spf policy?

Answer:
This SOP explains the bounce error “MailBox not found Remote host said: 550 5.7.0 message rejected per spf policy ?”, which occurs when the recipient mail server rejects the email due to SPF policy failure or remote host restrictions. -

Keywords: mailbox, not, found, remote, host, said, rejected, per, spf, policy, bounce

---

## Message Blocked Your message to abcd@testd.com has been blocked. See technical details below for more information. The response was Message bounces due to organizational settings

ID: `message_blocked_your_message_to_abcd_testd_com_has_been_blocked_see_technical_details_belo`
Category: Bounce
Subcategory: How To
Source section: Message Blocked Your message to abcd@testd.com has been blocked. See technical details below for more information. The response was Message bounces due to organizational settings

Alternate questions:
- How do I message blocked your message to abcd@testd.com has been blocked. see technical details below for more information. the response was message bounces due to organizational settings?
- How can I message blocked your message to abcd@testd.com has been blocked. see technical details below for more information. the response was message bounces due to organizational settings?

Answer:
This SOP explains the bounce error “Message Blocked Your message to abcd@testd.com has been blocked. See technical details below for more informati The response was Message bounces due to organizational settings”, which occurs due to restrictions applied by the recipient organization. -

Keywords: blocked, abcd, testd, com, has, been, see, technical, below, information, response, was

---

## Remote host said: 553 sorry, that domain isn't in my list of allowed rcpthosts; no valid cert for gatewaying (#5.7.1) ?Giving up on 119.252.155.52

ID: `remote_host_said_553_sorry_that_domain_isn_t_in_my_list_of_allowed_rcpthosts_no_valid_cert`
Category: Bounce
Subcategory: How To
Source section: Remote host said: 553 sorry, that domain isn't in my list of allowed rcpthosts; no valid cert for gatewaying (#5.7.1) ?Giving up on 119.252.155.52

Alternate questions:
- How do I remote host said: 553 sorry, that domain isn't in my list of allowed rcpthosts; no valid cert for gatewaying (#5.7.1) ?giving up on 119.252.155.52?
- How can I remote host said: 553 sorry, that domain isn't in my list of allowed rcpthosts; no valid cert for gatewaying (#5.7.1) ?giving up on 119.252.155.52?
- Why am I seeing Remote host said: 553 sorry, that domain isn't in my list of allowed rcpthosts; no valid cert for gatewaying (#5.7.1) ?Giving up on 119.252.155.52?

Answer:
This SOP explains the bounce error “Remote host said: 553 sorry, that domain isn't in my list of allowed rcpthosts; no valid cert for gatewaying (#5.7.1) ?Giving up on 119.252.155.52”, which occurs when the email services is hosted with Rediff but the email/MX services are not fully configured or were added recently. -

Keywords: remote, host, said, sorry, isn, list, allowed, rcpthosts, valid, cert, gatewaying, giving

---

## Requested action not taken: mailbox unavailable

ID: `requested_action_not_taken_mailbox_unavailable`
Category: Bounce
Subcategory: How To
Source section: Requested action not taken: mailbox unavailable

Alternate questions:
- How do I requested action not taken: mailbox unavailable?
- How can I requested action not taken: mailbox unavailable?

Answer:
This SOP explains the bounce error “Requested action not taken: mailbox unavailable”, which occurs when an email is sent to an email account that does not exist on the recipient mail server. -

Keywords: requested, action, not, taken, mailbox, unavailable, bounce

---

## Sorry, I couldn't find any host named <domain>” (#5.1.2)”, where <domain> can be any recipient domain

ID: `sorry_i_couldn_t_find_any_host_named_domain_5_1_2_where_domain_can_be_any_recipient_domain`
Category: Bounce
Subcategory: How To
Source section: Sorry, I couldn't find any host named <domain>” (#5.1.2)”, where <domain> can be any recipient domain.

Alternate questions:
- How do I sorry, i couldn't find any host named <domain>” (#5.1.2)”, where <domain> can be any recipient domain?
- How can I sorry, i couldn't find any host named <domain>” (#5.1.2)”, where <domain> can be any recipient domain?
- Why am I seeing Sorry, I couldn't find any host named <domain>” (#5.1.2)”, where <domain> can be any recipient domain?

Answer:
This SOP explains the bounce error “Sorry, I couldn't find any host named <domain> (#5.1.2)”, which occurs when the recipient domain dns/mx cannot be found by the mail server. -

Keywords: sorry, couldn, find, host, named, recipient, bounce

---

## Sorry, I wasn't able to establish an SMTP connection with <domain>”25 (#4.4.1) I'm not going to try again; this message has been in the queue too long. where <domain> can be any recipient domain

ID: `sorry_i_wasn_t_able_to_establish_an_smtp_connection_with_domain_25_4_4_1_i_m_not_going_to_`
Category: Bounce
Subcategory: How To
Source section: Sorry, I wasn't able to establish an SMTP connection with <domain>”25 (#4.4.1) I'm not going to try again; this message has been in the queue too long. where <domain> can be any recipient domain.

Alternate questions:
- How do I sorry, i wasn't able to establish an smtp connection with <domain>”25 (#4.4.1) i'm not going to try again; this message has been in the queue too long. where <domain> can be any recipient domain?
- How can I sorry, i wasn't able to establish an smtp connection with <domain>”25 (#4.4.1) i'm not going to try again; this message has been in the queue too long. where <domain> can be any recipient domain?
- Why am I seeing Sorry, I wasn't able to establish an SMTP connection with <domain>”25 (#4.4.1) I'm not going to try again; this message has been in the queue too long. where <domain> can be any recipient domain?

Answer:
This SOP explains the bounce error “Sorry, I wasn't able to establish an SMTP connection with <domain>:25 (#4.4.1) I'm not going to try again; this message has been in the queue too long.” where <domain> can be any recipient domain, which occurs when the sender mail server is unable to establish an SMTP connection with the recipient mail server. -

Keywords: sorry, wasn, able, establish, smtp, connection, not, going, try, again, has, been

---

## Sorry, no mailbox here by that name. (#5.1.1)

ID: `sorry_no_mailbox_here_by_that_name_5_1_1`
Category: Bounce
Subcategory: How To
Source section: Sorry, no mailbox here by that name. (#5.1.1)

Alternate questions:
- How do I sorry, no mailbox here by that name. (#5.1.1)?
- How can I sorry, no mailbox here by that name. (#5.1.1)?
- Why am I seeing Sorry, no mailbox here by that name. (#5.1.1)?

Answer:
This SOP explains the bounce error “Sorry, no mailbox here by that name. (#5.1.1)”, which occurs when an email is sent to an address that does not exist on the recipient domain. -

Keywords: sorry, mailbox, here, name, bounce

---

## The email you are trying to send is rejected due to Mail-Filtering policy . Please check with the administrator (#5.3.1)

ID: `the_email_you_are_trying_to_send_is_rejected_due_to_mail_filtering_policy_please_check_wit`
Category: Bounce
Subcategory: How To
Source section: The email you are trying to send is rejected due to Mail-Filtering policy . Please check with the administrator (#5.3.1)

Alternate questions:
- How do I the email you are trying to send is rejected due to mail-filtering policy . please check with the administrator (#5.3.1)?
- How can I the email you are trying to send is rejected due to mail-filtering policy . please check with the administrator (#5.3.1)?
- Why am I seeing The email you are trying to send is rejected due to Mail-Filtering policy . Please check with the administrator (#5.3.1)?

Answer:
This SOP explains the bounce error: “The email you are trying to send is rejected due to Mail-Filtering policy. Please check with the administrator (#5.3.1)”, which is received after attempting to send an email, when the message is rejected due to a mail-filtering policy configured by the email administrator. In Rediffmail Enterprise email services, administrators can configure mail-filtering policies that control outgoing emails. If an outgoing message violates any defined policy, the email is rejected and a bounce notification is generated. -

Keywords: trying, send, rejected, mail-filtering, policy, check, administrator, bounce

---

## The user is not allowed to receive mails from you. Please check with recipient

ID: `the_user_is_not_allowed_to_receive_mails_from_you_please_check_with_recipient`
Category: Bounce
Subcategory: How To
Source section: The user is not allowed to receive mails from you. Please check with recipient.

Alternate questions:
- How do I the user is not allowed to receive mails from you. please check with recipient?
- How can I the user is not allowed to receive mails from you. please check with recipient?

Answer:
This SOP explains the bounce error: “The user is not allowed to receive mails from you. Please check with recipient.” This error occurs when the recipient’s email administrator has applied an Incoming Mail Restriction under Other Services → Incoming Mail Restrictions or Group Policy >> Policy Management in Rediffmail Enterprise email services. Incoming mail restrictions allow administrators to control which senders or domains are permitted to send emails to specific users or to the entire domain. When an email violates these restrictions, the message is rejected and a bounce notification is generated. -

Keywords: not, allowed, receive, check, recipient, bounce

---

## The user is not allowed to receive mails with attachments of certain type/size. Please check with recipient

ID: `the_user_is_not_allowed_to_receive_mails_with_attachments_of_certain_type_size_please_chec`
Category: Bounce
Subcategory: How To
Source section: The user is not allowed to receive mails with attachments of certain type/size. Please check with recipient.

Alternate questions:
- How do I the user is not allowed to receive mails with attachments of certain type/size. please check with recipient?
- How can I the user is not allowed to receive mails with attachments of certain type/size. please check with recipient?

Answer:
This SOP explains the bounce error: “The user is not allowed to receive mails with attachments of certain type/size. Please check with recipient.” This error occurs when the recipient’s email administrator has configured Incoming Attachment Restrictions under Domain Level Management or Group Policy under Policy Management in Rediffmail Enterprise email services. Incoming attachment restrictions allow administrators to control and restrict emails containing attachments based on file type or file size. When an incoming email violates these configured attachment rules, the message is rejected and a bounce notification is generated. -

Keywords: not, allowed, receive, attachments, certain, type, size, check, recipient, bounce

---

## The user is not allowed to receive this mail because of the Filtering policy. Please check with the recipient's domain administrator

ID: `the_user_is_not_allowed_to_receive_this_mail_because_of_the_filtering_policy_please_check_`
Category: Bounce
Subcategory: How To
Source section: The user is not allowed to receive this mail because of the Filtering policy. Please check with the recipient's domain administrator.

Alternate questions:
- How do I the user is not allowed to receive this mail because of the filtering policy. please check with the recipient's domain administrator?
- How can I the user is not allowed to receive this mail because of the filtering policy. please check with the recipient's domain administrator?

Answer:
This SOP explains the bounce error “The user is not allowed to receive this mail because of the Filtering policy. Please check with the recipient's domain administrator.”, which occurs when incoming emails are blocked due to a mail filtering policy configured by the administrator. In Rediffmail Enterprise email services, administrators can create and apply email filtering policies that restrict incoming emails based on specific sender domains, sender email IDs, keywords, or other criteria. If such a policy is applied to a user account, emails matching the defined conditions will be rejected, resulting in this bounce message. -

Keywords: not, allowed, receive, filtering, policy, check, recipient, administrator, bounce

---

## What happens as a Rediffmail Enterprise Customer if DNS records are not configured correctly?

ID: `what_happens_as_a_rediffmail_enterprise_customer_if_dns_records_are_not_configured_correct`
Category: DNS
Subcategory: FAQ
Source section: Common FAQ: DNS Records Not Pointing Properly

Alternate questions:
- How do I what happens as a rediffmail enterprise customer if dns records are not configured correctly?
- How can I what happens as a rediffmail enterprise customer if dns records are not configured correctly?

Answer:
If DNS records are incorrect or missing: Then incoming Emails may not be delivered or received. Outgoing emails may go to Recipient domains Spam/Junk folders. - Your Website or Webmail Url may not open or open incorrectly - Email authentication may fail with other mail servers

Keywords: happens, customer, dns, records, not, configured, correctly, faq

---

## What is an A Record and what issues occur if it’s wrong?

ID: `what_is_an_a_record_and_what_issues_occur_if_it_s_wrong`
Category: DNS
Subcategory: FAQ
Source section: Common FAQ: DNS Records Not Pointing Properly

Alternate questions:
- How do I an a record and what issues occur if it’s wrong?
- How can I an a record and what issues occur if it’s wrong?

Answer:
A Record maps your domain to a server IP address. Common issues if incorrect: - Website not loading - Webmail or hosted services not accessible Check: Ensure the A record in Rediff DNS panel points to the correct IP provided by your hosting provider.:

Keywords: record, issues, occur, wrong, dns, faq

---

## What is an MX Record and why is it critical?

ID: `what_is_an_mx_record_and_why_is_it_critical`
Category: DNS
Subcategory: FAQ
Source section: Common FAQ: DNS Records Not Pointing Properly

Alternate questions:
- How do I an mx record and why is it critical?
- How can I an mx record and why is it critical?

Answer:
MX (Mail Exchange) Records tell the internet where to deliver emails for your domain, What happens as a Rediffmail Enterprise Customer? Common issues if incorrect: - Not receiving emails - Emails bouncing back to senders - Emails delivered to the wrong mail server Check: - Remove old or incorrect MX records - Make sure only the Rediffmail Enterprise MX records are present

Keywords: record, critical, dns, faq

---

## What is DKIM and why is it important?

ID: `what_is_dkim_and_why_is_it_important`
Category: DNS
Subcategory: FAQ
Source section: Common FAQ: DNS Records Not Pointing Properly

Alternate questions:
- How do I dkim and why is it important?
- How can I dkim and why is it important?

Answer:
DKIM (DomainKeys Identified Mail) digitally signs outgoing emails to prove they were not altered, What happens as a Rediffmail Enterprise Customer? Common issues if incorrect or missing: - Emails failing authentication - Reduced email deliverability - Emails landing in spam folders Check: - DKIM public key must be added exactly as provided You should make sure that the Selector provider by Rediffmail Enterprise and record name are matching correctly.

Keywords: dkim, important, dns, faq

---

## What is SPF and what happens if it’s missing or wrong?

ID: `what_is_spf_and_what_happens_if_it_s_missing_or_wrong`
Category: DNS
Subcategory: FAQ
Source section: Common FAQ: DNS Records Not Pointing Properly

Alternate questions:
- How do I spf and what happens if it’s missing or wrong?
- How can I spf and what happens if it’s missing or wrong?

Answer:
SPF (Sender Policy Framework) specifies which servers are allowed to send emails on behalf of your domain, What happens as a Rediffmail Enterprise Customer? Common issues if incorrect: - Outgoing emails marked as Spam - Emails rejected by recipient servers Check: - Ensure SPF includes all authorized mail servers If you are using multiple email service provider for same domain. In such condition, only one SPF record should exist per domain. It will be a merged SPF having records of 2 or more service providers.

Keywords: spf, happens, missing, wrong, dns, faq

---

## Which DNS records do I need to configure for Rediffmail Enterprise email and webmail?

ID: `which_dns_records_do_i_need_to_configure_for_rediffmail_enterprise_email_and_webmail`
Category: DNS
Subcategory: Configuration
Source section: DNS with Rediffmail Enterprise Emails

Alternate questions:
- How do I which dns records do i need to configure for rediffmail enterprise email and webmail?
- How can I which dns records do i need to configure for rediffmail enterprise email and webmail?

Answer:
- DNS with Rediffmail Enterprise Emails Rediffmail Enterprise is a cloud-based business email hosting service that gives you professional email addresses on your own domain (like you@yourcompany.com) instead of generic free mail IDs. It’s designed for businesses that want secure, reliable, and manageable email for employees and teams. They also facilitates domain booking/registration as part of its business email hosting process, so you can register a domain through them and then set up your professional email on that domain or you might already have a domain from any other domain service provider like Godaddy, Hostinger.in and you can host your emails with Rediffmail Enterprise. They offer a selection of common extensions (e.g.,.com,.in,.net,.org,.biz, etc.) that you can choose from if the name is available. You can purchase the domain for multiple years (often 1–5 years initially) and then use it for your email hosting and business presence online. So, when you book a domain with Rediffmail Enterprise you get a Domain Contol Panel to manage DNS and other domain related services. Rediffmail Enterprise has their own nameservers i.e ns.rediffmailpro.com and ns2.rediffmailpro.com. Every customer buying their domain services with Rediffmail Enterprise by default gets their nameservers pointed. If you want to use Rediffmail Enterprise DNS services then you should have your domain also with them. You can transfer your domain from any other service provider to them and then use their DNS services. You can manage the domain i.e add/update/delete the DNS records of your domain through the Domain Control Panel provided by Rediffmail Enterprise. So, if you take - Only Domain Services then you get Domain Control Panel - Only Email Services then you get only Email Administration Panel Domain + Email Services then you get both Domain Control Panel and Email Administration Panel. - Different Types of DNS records that Rediffmail Enterprise has - MX records Point the MX records of the <domain>. - Type MX Host @ - Value mail.rediffmailpr.com - Preference / Priority 10 - TTL default or minimum possible This record is very important to activate your account. If you have taken Domain services with Rediffmail Enterprise then the MX records will get created by default however if you have domain from any other service provider and email services from Rediffmail Enterprise then you will need to point the MX of your domain to Rediff. Some of the Tutorial is Godaddy Video Tutorial - https://support.rediffmailpro.com/article/godaddy-mx-a-record-updation-for-email-activation - Bigrock Video Tutorial - https://support.rediffmailpro.com/article/bigrock-mx-a-record-updation-for-email-activation Webmail You get custom webmail setup with Rediffmail Enterprise. To activate the same, you need to point the cname record for your webmail - Type CNAME Host mail / webmail / email - Value platform.rediffmailpro.com TTL default or minimum possible This will help you access the emails over the web interface. You need to add this in your DNS records. There is also a common url available i.e https://webmail.rediffmailpro.com/action/login/<yourdomain> - Until you make DNS changes you can use this URL for your webmail access. You just need to put your domain in the end. Example if my domain is cshelp.in then the url will be https://webmail.rediffmailpro.com/action/login/cshelp.in. SPF records SPF records are a type of DNS TXT record commonly used for email authentication. Type TXT - Host: @ Value: v spf1 redirect _spf.rediffmailpro.com If you have taken Domain services with Rediffmail Enterprise then the SPF records will get created by default however if you have domain from any other service provider and email services from Rediffmail Enterprise then you will need to point the SPF of your domain to Rediff. In some cases, there is a possibility that your have a same domain with using email services from 2 different email service providers like M365 and Rediff. In such cases there should be MX records of both the service providers. So, kindly connect with our support team to discuss this. - DKIM records Type: TXT - Host: mail._domainkey Value: v DKIM1; k rsa;p MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuwIb0JCNtN0Ugzm+CKinJQdSYhrbGtiglj52+EAkn5CXnJ9B8utUGHqFeSXq3dkguZkSKScLaV+Zv/G3cSY90asURuBssxdQ28WuW96IMRiO0E0QpcydDjFVMh1wvOx+HSXF2yjMCph4IeQrX3Q2Ehs496ZY0h7I2pHxen2Bul+RTLXDbYgdT5oFYUykVUPl+NyWNr2GQ1OYxiolzRQsnWMyzocCCF8cMXj1Vg061dnmlM/SahLwp8rxGJbQV8WFZ1YlAzDLGyJCuIg4D1xZTWd3KhqDFpnoeNp3gXQlz475YY1NLlGqeiibId+NARMtGxnjWCWiKwenp00sod7MmQIDAQAB In some cases, there is a possibility that your have a same domain with using email services from 2 different email service providers like M365 and Rediff. In such cases there should be MX records of both the service providers. So, kindly connect with our support team to discuss this. A records If you have taken domain services from Rediff then you can edit/add/delete A record from the Domain Control Panel provided by Rediffmail Enterprise. You can have your website pointing to some other service provider and your emails can function from Rediffmail Enterprise. You just need to keep your DNS records proper. In all the mentioned DNS records, if the Nameservers are with Rediff then the necessary DNS records changes can be done through Domain Control Panel provided by Rediff But If the Name Servers are pointing to any other service provider like Godaddy, Hostinger, etc… then you need to contact their support team and make necessary changes in their DNS panel.

Keywords: which, dns, records, need, configuration

---

## You are not allowed to send mails to this domain. Please contact recipient's domain administrator

ID: `you_are_not_allowed_to_send_mails_to_this_domain_please_contact_recipient_s_domain_adminis`
Category: Bounce
Subcategory: How To
Source section: You are not allowed to send mails to this domain. Please contact recipient's domain administrator

Alternate questions:
- How do I you are not allowed to send mails to this domain. please contact recipient's domain administrator?
- How can I you are not allowed to send mails to this domain. please contact recipient's domain administrator?

Answer:
This SOP explains the bounce error “You are not allowed to send mails to this domain. Please contact recipient's domain administrator”, which occurs when a user is restricted from sending emails to a specific recipient domain. Rediffmail Enterprise includes an administrative control that enables administrators to block incoming emails from specific domains for selected users or across the entire domain. -

Keywords: not, allowed, send, contact, recipient, administrator, bounce

---

## You are not allowed to send mails to this Email ID as per the policy set by your administrator. Please contact your administrator for further details. (#4.3.0)

ID: `you_are_not_allowed_to_send_mails_to_this_email_id_as_per_the_policy_set_by_your_administr`
Category: Bounce
Subcategory: How To
Source section: You are not allowed to send mails to this Email ID as per the policy set by your administrator. Please contact your administrator for further details. (#4.3.0)

Alternate questions:
- How do I you are not allowed to send mails to this email id as per the policy set by your administrator. please contact your administrator for further details. (#4.3.0)?
- How can I you are not allowed to send mails to this email id as per the policy set by your administrator. please contact your administrator for further details. (#4.3.0)?
- Why am I seeing You are not allowed to send mails to this Email ID as per the policy set by your administrator. Please contact your administrator for further details. (#4.3.0)?

Answer:
This SOP explains the bounce error: “You are not allowed to send mails to this Email ID as per the policy set by your administrator. Please contact your administrator for further details. (#4.3.0)” This error occurs when the email administrator has applied an Outgoing Email Restriction under Other Services → Restrict Outgoing Emails in Rediffmail Enterprise. Outgoing mail restrictions allow administrators to control and restrict outgoing emails to specific email IDs or domains. When an outgoing message violates these configured restrictions, the system rejects the email and generates this bounce message. -

Keywords: not, allowed, send, per, policy, administrator, contact, further, bounce

---

## You Do Not Have Permission to Send This Message to This Distribution List

ID: `you_do_not_have_permission_to_send_this_message_to_this_distribution_list`
Category: Bounce
Subcategory: How To
Source section: You Do Not Have Permission to Send This Message to This Distribution List

Alternate questions:
- How do I you do not have permission to send this message to this distribution list?
- How can I you do not have permission to send this message to this distribution list?

Answer:
This SOP explains the bounce error: “You do not have permission to send this message to this Distribution List.” This error occurs when a user attempts to send an email to a mailing list (distribution group) without having the required sending permissions. In Rediffmail Enterprise email services, administrators can create mailing lists (groups) and define sender permissions to control who is allowed to send emails to those mailing lists. If the sender is not included in the allowed list, the email is rejected and a bounce notification is generated. -

Keywords: not, have, permission, send, distribution, list, bounce

---

## You have been blocked by the recipient

ID: `you_have_been_blocked_by_the_recipient`
Category: Bounce
Subcategory: How To
Source section: You have been blocked by the recipient

Alternate questions:
- How do I you have been blocked by the recipient?
- How can I you have been blocked by the recipient?

Answer:
This SOP explains the bounce error “You have been blocked by the recipient”, which occurs when the recipient using Rediffmail Enterprise email services has blocked the sender’s email address. -

Keywords: have, been, blocked, recipient, bounce

---
