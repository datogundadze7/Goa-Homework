# Flexbox თვისებები და მათი მნიშვნელობები

flexbox_properties = {
    "justify-content": {
        "description": "განმარტავს როგორ არის განლაგებული და განაწილებული ფლექს ელემენტები მთავარ ღერძზე.",
        "values": {
            "flex-start": "ელემენტები განლაგდებიან კონტეინერის დასაწყისში (მარცხნივ).",
            "flex-end": "ელემენტები განლაგდებიან კონტეინერის ბოლოში (მარჯვნივ).",
            "center": "ელემენტები განლაგდებიან ჰორიზონტალურად ცენტრში.",
            "space-between": "ელემენტებს შორის თანაბარი სივრცე იქნება, ხოლო პირველი და ბოლო ელემენტები კონტეინერის კიდეებთან იქნება.",
            "space-around": "ელემენტებს შორის თანაბარი სივრცეა, კონტეინერის კიდეებს შორისაც გარკვეული სივრცე რჩება.",
            "space-evenly": "ელემენტებს შორის სივრცე თანაბრად არის განაწილებული, მათ შორის და კიდეებს შორისაც."
        }
    },
    "align-items": {
        "description": "განმარტავს როგორ არის განლაგებული ფლექს ელემენტები გვერდითი ღერძზე.",
        "values": {
            "stretch": "ელემენტები იჭიმებიან კონტეინერის სიმაღლეზე (ნაგულისხმევი).",
            "flex-start": "ელემენტები განლაგდებიან ღერძის დასაწყისში (ზემოთ).",
            "flex-end": "ელემენტები განლაგდებიან ღერძის ბოლოში (ქვემოთ).",
            "center": "ელემენტები განლაგდებიან ვერტიკალურად ცენტრში.",
            "baseline": "ელემენტები განლაგდებიან ტექსტის საწყის ხაზზე."
        }
    },
    "flex-direction": {
        "description": "განმარტავს ფლექს ელემენტების მიმართულებას მთავარ ღერძზე.",
        "values": {
            "row": "ელემენტები განლაგდებიან ჰორიზონტალურად, მარცხნიდან მარჯვნივ (ნაგულისხმევი).",
            "row-reverse": "ელემენტები განლაგდებიან ჰორიზონტალურად, მარჯვნიდან მარცხნივ.",
            "column": "ელემენტები განლაგდებიან ვერტიკალურად, ზემოდან ქვემოთ.",
            "column-reverse": "ელემენტები განლაგდებიან ვერტიკალურად, ქვემოდან ზემოთ."
        }
    },
    "order": {
        "description": "განმარტავს ფლექს ელემენტების თანმიმდევრობას კონტეინერის შიგნით.",
        "values": {
            "number": "ხაზოვანი რიცხვი. ნაგულისხმევი მნიშვნელობაა 0. უფრო მცირე რიცხვები გამოჩნდება უფრო ადრე."
        }
    },
    "align-self": {
        "description": "შეიძლება გადაჭრას ცალკეული ელემენტების განლაგება სხვა ელემენტებისგან განსხვავებით.",
        "values": {
            "auto": "მემკვიდრეობით იღებს align-items-ის მნიშვნელობას (ნაგულისხმევი).",
            "flex-start": "ელემენტი განლაგდება ღერძის დასაწყისში (ზემოთ).",
            "flex-end": "ელემენტი განლაგდება ღერძის ბოლოში (ქვემოთ).",
            "center": "ელემენტი განლაგდება ვერტიკალურად ცენტრში.",
            "baseline": "ელემენტი განლაგდება ტექსტის საწყის ხაზთან.",
            "stretch": "ელემენტი გაჭიმულია, რომ შეესაბამებოდეს კონტეინერის სიმაღლეს."
        }
    },
    "flex-wrap": {
        "description": "განმარტავს, უნდა გადაინაცვლოს თუ არა ფლექს ელემენტებს ახალ ხაზზე.",
        "values": {
            "nowrap": "ყველა ელემენტი დარჩება ერთ ხაზზე (ნაგულისხმევი).",
            "wrap": "ელემენტები გადავლენ ახალ ხაზზე საჭიროების შემთხვევაში.",
            "wrap-reverse": "ელემენტები გადავლენ ახალ ხაზზე უკუღმა (ბოლო ხაზი იქნება ზემოთ)."
        }
    },
    "flex-flow": {
        "description": "Flex-direction და flex-wrap თვისებების შერწყმა.",
        "values": {
            "direction wrap": "შეერთებს flex-direction და flex-wrap. მაგალითად: 'row wrap'.",
            "column nowrap": "შეერთებს flex-direction და flex-wrap. მაგალითად: 'column nowrap'."
        }
    },
    "align-content": {
        "description": "განმარტავს როგორ არის განლაგებული ფლექს ხაზები კონტეინერის შიგნით.",
        "values": {
            "flex-start": "ხაზები გაწვდება კონტეინერის დასაწყისში.",
            "flex-end": "ხაზები გაწვდება კონტეინერის ბოლოში.",
            "center": "ხაზები განლაგდება ვერტიკალურად ცენტრში.",
            "space-between": "ხაზები თანაბრად განაწილდება სივრცით.",
            "space-around": "ხაზები თანაბრად განაწილდება სივრცით, თუმცა კიდეებს შორისაც მცირე სივრცე რჩება.",
            "stretch": "ხაზები გაჭიმულია, რომ შეესაბამებოდეს კონტეინერს (ნაგულისხმევი)."
        }
    }
}

# დაბეჭდეთ თითოეული თვისება მისი აღწერით და მნიშვნელობებით
for property_name, property_info in flexbox_properties.items():
    print(f"{property_name.capitalize()}:")
    print(f"  აღწერა: {property_info['description']}")
    for value, definition in property_info['values'].items():
        print(f"  - {value}: {definition}")
    print()