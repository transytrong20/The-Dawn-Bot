# Bot for Dawn Extension (Docker version)

## 🔗 Links

🔔 CHANNEL: https://t.me/JamBitPY

💬 CHAT: https://t.me/JamBitChat

💰 DONATION EVM ADDRESS: 0xe23380ae575D990BebB3b81DB2F90Ce7eDbB6dDa



## ⚙️ Config (config > settings.yaml):

```
Accounts: data > farm.txt | Format:
- email:password

Proxies: data > proxies.txt | Format:
- type://user:pass@ip:port (http/socks5)
- type://user:pass:ip:port (http/socks5)
- type://ip:port:user:pass (http/socks5)
- type://ip:port@user:pass (http/socks5)
```


| Name              | Description                                      |
|-------------------|--------------------------------------------------|
| threads           | Number of accounts that will work simultaneously |
| anti_captcha_api_key             | anti-captcha api key                             |
| keepalive_interval             | delay between keepalive requests in seconds      |



## 🚀 | How to start:
1. **Close the repo and open CMD (console) inside it**
```bash
git clone this repo
```

2. **Setup configuration and accounts**

3. **Build and Run:**
```bash
docker-compose up -d --build
```
