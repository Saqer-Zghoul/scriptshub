import requests

CLOUD_API_URL = "https://scripthub-dk5j.onrender.com"  
CLOUD_API_KEY = "my-super-secret-key-123"

def run_ip_checker(request):
    ip_address = request.POST.get('ip_address', '').strip()
    if not ip_address:
        return None

    endpoint = f"{CLOUD_API_URL}/api/v1/ip-checker"
    headers = {"X-API-KEY": CLOUD_API_KEY}
    
    try:
        response = requests.post(endpoint, json={"ip": ip_address}, headers=headers, timeout=10)
        if response.status_code == 200:
            res_json = response.json()
            if res_json.get("status") == "success":
                data = res_json.get("data", {})
                lat, lon = data.get('lat'), data.get('lon')
                return {
                    "status": "success",
                    "ip": data.get('query'),
                    "country": data.get('country'),
                    "country_code": data.get('countryCode'),
                    "region": data.get('regionName'),
                    "city": data.get('city'),
                    "isp": data.get('isp'),
                    "org": data.get('org', 'غير محدد'),
                    "as_number": data.get('as'),
                    "maps_url": f"https://www.google.com/maps?q={lat},{lon}" if lat and lon else None,
                }
            return {"status": "error", "message": res_json.get("message")}
        return {"status": "error", "message": f"خطأ من سيرفر السحابة: {response.status_code}"}
    except Exception as e:
        return {"status": "error", "message": f"تعذر الاتصال بالسحابة: {str(e)}"}


# الدالة التي يبحث عنها views.py
def execute_script(script_slug, request):
    """توجيه الطلب للسكريبت المناسب بناءً على الـ slug"""
    if script_slug == 'ip-checker' or script_slug == 'ip-lookup':
        return run_ip_checker(request)
    
    # يمكن إضافة سكريبتات أخرى هنا مستقبلاً
    return None