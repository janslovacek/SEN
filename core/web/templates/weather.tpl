% rebase('base.tpl', title='Current weather', page='weather')

<div id="weather">
    <div class="row">
        <div class="col-md-3">
            <div class="card">
                <h5 class="card-header">Temperature</h5>
                <div class="card-block">
                    <h1 class="card-title">{{record[1]}} °C</h1>
                </div>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card">
                <h5 class="card-header">Humidity</h5>
                <div class="card-block">
                    <h1 class="card-title">{{record[2]}} %</h1>
                </div>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card">
                <h5 class="card-header">Air pressure</h5>
                <div class="card-block">
                    <h1 class="card-title">{{record[3] // 100}} hPa</h1>
                </div>
            </div>
        </div>
        <%
        from helper import IO
        sky_status = IO.get_cloud_value(record[4], record[5], record[6], record[7])
        %>

        <%
        sky_status_str = None
        if sky_status == 0:
            sky_status_str = "Night"
        elif sky_status == 1:
            sky_status_str = "Cloudy"
        elif sky_status == 2:
            sky_status_str = "Partly cloudy"
        elif sky_status == 3:
            sky_status_str = "Clear sky"
        end
        %>

        <div class="col-md-3">
            <div class="card">
                <h5 class="card-header">Sky status</h5>
                <div class="card-block">
                    <h1 class="card-title">{{sky_status_str}}</h1>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12 text-md-right">
            <%
            from datetime import datetime
            date_time = datetime.fromtimestamp(record[8]/1000.0)
            date = date_time.strftime('%B %e %Y')
            time = date_time.strftime('%H:%M')
            %>
            <small>Last measurement was made in {{date}} at {{time}} </small>
        </div>
    </div>
</div>