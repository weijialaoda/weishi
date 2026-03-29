"""
使用 PIL 创建 PWA 图标（如果可用），否则直接复制
"""
import os
import shutil

# 源图片路径
source_image = r"C:\Users\Administrator\.real\users\user-d11b7c7ffb5ea17fb529446a5fc99972\workspace\generated_image_1774772724339.jpg"

# 输出目录
output_dir = r"C:\Users\Administrator\.real\users\user-d11b7c7ffb5ea17fb529446a5fc99972\workspace\expense_tracker"

try:
    from PIL import Image
    
    # 打开图片
    img = Image.open(source_image)
    
    # 创建 192x192 图标
    icon_192 = img.resize((192, 192), Image.LANCZOS)
    icon_192_path = os.path.join(output_dir, "icon-192.png")
    icon_192.save(icon_192_path, "PNG")
    print(f"✓ 已创建：icon-192.png (192x192)")
    
    # 创建 512x512 图标
    icon_512 = img.resize((512, 512), Image.LANCZOS)
    icon_512_path = os.path.join(output_dir, "icon-512.png")
    icon_512.save(icon_512_path, "PNG")
    print(f"✓ 已创建：icon-512.png (512x512)")
    
    print("\n✅ PWA 图标创建完成！")
    
except ImportError:
    print("PIL 不可用，直接复制原图...")
    # 直接复制并重命名
    shutil.copy2(source_image, os.path.join(output_dir, "icon-192.png"))
    shutil.copy2(source_image, os.path.join(output_dir, "icon-512.png"))
    print("✓ 已复制图片（未调整尺寸）")
    print("\n⚠️ 建议手动调整图片尺寸为 192x192 和 512x512")
