from MapAvro import AvroConverter

converter = AvroConverter()

bengali = "আমি বাংলায় গান গাই। আমি আমার আমিকে চিরদিন এই বাংলায় খুজে পাই। বাংলাদেশ একটি ছোট রাষ্ট্রে।"
print(bengali)

avro = converter.bengali_to_avro(bengali)
print(avro)

bengali = converter.avro_to_bengali(avro)
print(bengali)