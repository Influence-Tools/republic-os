---
type: Jurisdiction
title: "Clarke County, GA"
classification: county
fips: "13059"
state: "GA"
demographics:
  population: 129609
  population_under_18: 21685
  population_18_64: 91724
  population_65_plus: 16200
  median_household_income: 53625
  poverty_rate: 26.05
  homeownership_rate: 41.43
  unemployment_rate: 5.25
  median_home_value: 298900
  gini_index: 0.5014
  vacancy_rate: 5.98
  race_white: 73767
  race_black: 33281
  race_asian: 5451
  race_native: 664
  hispanic: 15269
  bachelors_plus: 53476
districts:
  - to: "us/states/ga/districts/10"
    rel: in-district
    area_weight: 0.9979
  - to: "us/states/ga/districts/senate/47"
    rel: in-district
    area_weight: 0.6285
  - to: "us/states/ga/districts/senate/46"
    rel: in-district
    area_weight: 0.3714
  - to: "us/states/ga/districts/house/122"
    rel: in-district
    area_weight: 0.3903
  - to: "us/states/ga/districts/house/121"
    rel: in-district
    area_weight: 0.2338
  - to: "us/states/ga/districts/house/120"
    rel: in-district
    area_weight: 0.2112
  - to: "us/states/ga/districts/house/124"
    rel: in-district
    area_weight: 0.1646
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Clarke County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 129609 |
| Under 18 | 21685 |
| 18–64 | 91724 |
| 65+ | 16200 |
| Median household income | 53625 |
| Poverty rate | 26.05 |
| Homeownership rate | 41.43 |
| Unemployment rate | 5.25 |
| Median home value | 298900 |
| Gini index | 0.5014 |
| Vacancy rate | 5.98 |
| White | 73767 |
| Black | 33281 |
| Asian | 5451 |
| Native | 664 |
| Hispanic/Latino | 15269 |
| Bachelor's or higher | 53476 |

## Districts

- [GA-10](/us/states/ga/districts/10.md) — 100% (congressional)
- [GA Senate District 47](/us/states/ga/districts/senate/47.md) — 63% (state senate)
- [GA Senate District 46](/us/states/ga/districts/senate/46.md) — 37% (state senate)
- [GA House District 122](/us/states/ga/districts/house/122.md) — 39% (state house)
- [GA House District 121](/us/states/ga/districts/house/121.md) — 23% (state house)
- [GA House District 120](/us/states/ga/districts/house/120.md) — 21% (state house)
- [GA House District 124](/us/states/ga/districts/house/124.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
