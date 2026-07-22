import numpy as np
import time
import matplotlib.pyplot as plt
def load_stock_data():
    np.random.seed(42)
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    n = 120
    prices = []
    weekdays = []
    month_names = []
    chg_pct = []
    base_price = 5000
    for i in range(n):
        change = np.random.normal(0, 1.5)
        base_price = base_price + change * 10
        if base_price < 4500:
            base_price = 4500
        prices.append(base_price)
        chg_pct.append(change)
        weekdays.append(days_of_week[i % 5])
        month_names.append(months[i // 20])
    return np.array(prices), np.array(chg_pct), weekdays, month_names
def my_mean(data):
    total = 0
    count = 0
    for val in data:
        total = total + val
        count = count + 1
    return total / count
def my_variance(data):
    mean_val = my_mean(data)
    total = 0
    count = 0
    for val in data:
        total = total + (val - mean_val) ** 2
        count = count + 1
    return total / count
if __name__ == "__main__":
    prices, chg_pct, weekdays, months = load_stock_data()

    print("===== IRCTC Stock Price Analysis =====")
    print(f"total records: {len(prices)}")
    print(f"price range: Rs {min(prices):.2f} - Rs {max(prices):.2f}")
    print()
    np_mean = np.mean(prices)
    np_var = np.var(prices)
    print(f"[NUMPY] mean price: Rs {np_mean:.2f}")
    print(f"[NUMPY] variance: {np_var:.2f}")
    print()
    my_mean_val = my_mean(prices)
    my_var_val = my_variance(prices)
    print(f"[CUSTOM] mean price: Rs {my_mean_val:.2f}")
    print(f"[CUSTOM] variance: {my_var_val:.2f}")
    print()
    print(f"mean difference: {abs(np_mean - my_mean_val):.6f}")
    print(f"variance difference: {abs(np_var - my_var_val):.6f}")
    print()
    numpy_times = []
    custom_times = []
    for _ in range(10):
        t1 = time.time()
        np.mean(prices)
        np.var(prices)
        t2 = time.time()
        numpy_times.append(t2 - t1)
        t3 = time.time()
        my_mean(prices)
        my_variance(prices)
        t4 = time.time()
        custom_times.append(t4 - t3)

    print(f"avg numpy execution time: {np.mean(numpy_times)*1000:.4f} ms")
    print(f"avg custom execution time: {np.mean(custom_times)*1000:.4f} ms")
    print()
    wed_prices = []
    for i in range(len(prices)):
        if weekdays[i] == "Wed":
            wed_prices.append(prices[i])
    wed_mean = my_mean(wed_prices)
    print(f"[WEDNESDAY] sample mean: Rs {wed_mean:.2f}")
    print(f"[WEDNESDAY] population mean: Rs {np_mean:.2f}")
    print(f"  -> wednesday mean is {'higher' if wed_mean > np_mean else 'lower'} than population mean")
    print()
    apr_prices = []
    for i in range(len(prices)):
        if months[i] == "Apr":
            apr_prices.append(prices[i])
    if len(apr_prices) > 0:
        apr_mean = my_mean(apr_prices)
        print(f"[APRIL] sample mean: Rs {apr_mean:.2f}")
        print(f"[APRIL] population mean: Rs {np_mean:.2f}")
    print()
    loss_count = 0
    for val in chg_pct:
        if val < 0:
            loss_count = loss_count + 1
    prob_loss = loss_count / len(chg_pct)
    print(f"probability of making a loss: {prob_loss*100:.2f}%")
    print()
    wed_profit_count = 0
    wed_total = 0
    for i in range(len(chg_pct)):
        if weekdays[i] == "Wed":
            wed_total = wed_total + 1
            if chg_pct[i] > 0:
                wed_profit_count = wed_profit_count + 1
    prob_profit_wed = wed_profit_count / wed_total if wed_total > 0 else 0
    print(f"probability of profit on wednesday: {prob_profit_wed*100:.2f}%")
    print()

    # conditional prob
    cond_prob = wed_profit_count / wed_total if wed_total > 0 else 0
    print(f"conditional probability P(profit | wednesday): {cond_prob*100:.2f}%")
    print()

    # scatter plot
    day_num = []
    day_map = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4}
    for d in weekdays:
        day_num.append(day_map[d])
    plt.figure(figsize=(10, 5))
    plt.scatter(day_num, chg_pct, alpha=0.6, color="blue")
    plt.axhline(y=0, color="red", linestyle="--", linewidth=0.5)
    plt.xticks(range(5), ["Mon", "Tue", "Wed", "Thu", "Fri"])
    plt.xlabel("Day of Week")
    plt.ylabel("Chg%")
    plt.title("Chg% vs Day of Week (IRCTC Stock)")
    plt.grid(True, alpha=0.3)
    plt.savefig("stock_scatter.png", dpi=100)
    print("[PLOT] scatter plot saved as 'stock_scatter.png'")
