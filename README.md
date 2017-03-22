# unicode_subject
Decode email subject header to UTF8 (RFC 1342).

Expect subject header line to be streamed via stdin.

Created to be used with [FDM](https://github.com/nicm/fdm) in a `pipe` matching rule.


## Example

### Test example :
`echo "Subject: =?GB2312?B?zqrKssO00rW8qNfcsrvA7c/ro78=?=" | unicode_subject.py`

`Subject: 为什么业绩总不理想？`

### `fdm.conf` example :
`match pipe "python3 -sqI unicode_subject.py" returns (,"^Subject: ?[^a-zA-Z]*$") action maildir "%h/.Maildir/.spam"`
