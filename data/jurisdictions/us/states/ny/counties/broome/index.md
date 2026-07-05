---
type: Jurisdiction
title: "Broome County, NY"
classification: county
fips: "36007"
state: "NY"
demographics:
  population: 197378
  population_under_18: 37690
  population_18_64: 119652
  population_65_plus: 40036
  median_household_income: 62616
  poverty_rate: 18.49
  homeownership_rate: 64.53
  unemployment_rate: 7.09
  median_home_value: 154900
  gini_index: 0.4706
  vacancy_rate: 11.98
  race_white: 158412
  race_black: 11092
  race_asian: 10089
  race_native: 310
  hispanic: 10961
  bachelors_plus: 59354
districts:
  - to: "us/states/ny/districts/19"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/ny/districts/senate/51"
    rel: in-district
    area_weight: 0.5509
  - to: "us/states/ny/districts/senate/52"
    rel: in-district
    area_weight: 0.4487
  - to: "us/states/ny/districts/house/121"
    rel: in-district
    area_weight: 0.5824
  - to: "us/states/ny/districts/house/124"
    rel: in-district
    area_weight: 0.2224
  - to: "us/states/ny/districts/house/123"
    rel: in-district
    area_weight: 0.1391
  - to: "us/states/ny/districts/house/131"
    rel: in-district
    area_weight: 0.0558
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Broome County, NY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 197378 |
| Under 18 | 37690 |
| 18–64 | 119652 |
| 65+ | 40036 |
| Median household income | 62616 |
| Poverty rate | 18.49 |
| Homeownership rate | 64.53 |
| Unemployment rate | 7.09 |
| Median home value | 154900 |
| Gini index | 0.4706 |
| Vacancy rate | 11.98 |
| White | 158412 |
| Black | 11092 |
| Asian | 10089 |
| Native | 310 |
| Hispanic/Latino | 10961 |
| Bachelor's or higher | 59354 |

## Districts

- [NY-19](/us/states/ny/districts/19.md) — 100% (congressional)
- [NY Senate District 51](/us/states/ny/districts/senate/51.md) — 55% (state senate)
- [NY Senate District 52](/us/states/ny/districts/senate/52.md) — 45% (state senate)
- [NY House District 121](/us/states/ny/districts/house/121.md) — 58% (state house)
- [NY House District 124](/us/states/ny/districts/house/124.md) — 22% (state house)
- [NY House District 123](/us/states/ny/districts/house/123.md) — 14% (state house)
- [NY House District 131](/us/states/ny/districts/house/131.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
