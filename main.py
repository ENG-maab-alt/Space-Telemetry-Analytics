import os
import numpy as np
import matplotlib.pyplot as plt

try:
    # 1. تحديد مكان الملف الحالي
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # مصفوفة بالمسارات المحتملة لتجربتها تلقائياً
    possible_paths = [
        os.path.join(current_dir, 'data'),          
        os.path.join(current_dir, 'pr1', 'data'),   
        os.path.dirname(current_dir)                 
    ]
    
    data_dir = None
    npy_files = []
    
    # 2. البحث الذكي عن مجلد data الحاوي على ملفات .npy
    for path in possible_paths:
        if os.path.exists(path):
            files = [f for f in os.listdir(path) if f.endswith('.npy')]
            if files:
                data_dir = path
                npy_files = files
                break
                
    if not data_dir:
        for root, dirs, files in os.walk(current_dir):
            files = [f for f in files if f.endswith('.npy')]
            if files:
                data_dir = root
                npy_files = files
                break

    # 3. إذا عثرنا على المجلد، نقوم بالتحميل والرسم فوراً
    if data_dir and npy_files:
        target_file = npy_files[0]  # سنرسم أول ملف مصفوفة متاح A-1.npy
        file_path = os.path.join(data_dir, target_file)
        
        # تحميل البيانات
        sensor_data = np.load(file_path)
        
        # رسم السلسلة الزمنية للحساس
        plt.figure(figsize=(12, 5))
        plt.plot(sensor_data, color='crimson', linewidth=1.5, label='Sensor Readings')
        
        # إضافة اللمسات الاحترافية للوحة
        plt.title(f'Time Series Visualisation for Sensor: {target_file}', fontsize=14, fontweight='bold')
        plt.xlabel('Time Step (Index)', fontsize=12)
        plt.ylabel('Value', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        
        print(f"The file was found in:  {file_path}")
        print(f"The sensor timeline is now being generated and displayed {target_file}...")
        plt.show()
        
    else:
        print(" We could not find any .npy files in the project folders for plotting.")

except Exception as e:
    print(f"Error occurred during the plotting process: {e}")