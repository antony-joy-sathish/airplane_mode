# Copyright (c) 2025, deepak and contributors
# For license information, please see license.txt

import frappe
from frappe.query_builder import DocType, functions as fn, Order

def execute(filters=None):
    columns = [
        {"label": "Airline", "fieldname": "airline", "fieldtype": "Link", "options": "Airline", "width": 200},
        {"label": "Total Revenue", "fieldname": "total_revenue", "fieldtype": "Currency", "width": 150},
    ]

    Ticket = DocType("Airplane Ticket")
    Airline = DocType("Airline")

    query = (
        frappe.qb.from_(Ticket)
        .join(Airline)
        .on(Ticket.airline == Airline.name)
        .select(
            Ticket.airline,
            fn.Sum(Ticket.total_amount).as_("total_revenue"),
        )
        .groupby(Ticket.airline)
        .orderby(fn.Sum(Ticket.total_amount), order=Order.desc)
    )

    data = query.run(as_dict=True)

    # 🚀 Total Revenue
    total_revenue = sum(d["total_revenue"] for d in data)

    # ✅ Donut Chart
    chart = {
        "data": {
            "labels": [d["airline"] for d in data],
            "datasets": [{"values": [d["total_revenue"] for d in data]}],
        },
        "type": "donut",
        "height": 300,
    }

    # ✅ Report Summary
    summary = [
    {
        "label": "Total Revenue",
        "value": total_revenue,
        "indicator": "green",
        "datatype": "Currency",     # ✅ tells frappe it's money
        "currency": "INR",          # ✅ INR symbol will show
        "background-color": "gray-900"    # ✅ light gray background
    },
    ]


    # # ✅ Add Total Row
    # data.append({"airline": "Total", "total_revenue": total_revenue})

    return columns, data, None, chart, summary

