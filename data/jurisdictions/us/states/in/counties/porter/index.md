---
type: Jurisdiction
title: "Porter County, IN"
classification: county
fips: "18127"
state: "IN"
demographics:
  population: 174818
  population_under_18: 37321
  population_18_64: 105544
  population_65_plus: 31953
  median_household_income: 87972
  poverty_rate: 9.58
  homeownership_rate: 77.73
  unemployment_rate: 4.69
  median_home_value: 281500
  gini_index: 0.4343
  vacancy_rate: 5.54
  race_white: 146281
  race_black: 7813
  race_asian: 2597
  race_native: 202
  hispanic: 20367
  bachelors_plus: 52232
districts:
  - to: "us/states/in/districts/01"
    rel: in-district
    area_weight: 0.8036
  - to: "us/states/in/districts/senate/5"
    rel: in-district
    area_weight: 0.5225
  - to: "us/states/in/districts/senate/4"
    rel: in-district
    area_weight: 0.2815
  - to: "us/states/in/districts/house/4"
    rel: in-district
    area_weight: 0.3461
  - to: "us/states/in/districts/house/9"
    rel: in-district
    area_weight: 0.142
  - to: "us/states/in/districts/house/10"
    rel: in-district
    area_weight: 0.1395
  - to: "us/states/in/districts/house/19"
    rel: in-district
    area_weight: 0.1227
  - to: "us/states/in/districts/house/11"
    rel: in-district
    area_weight: 0.0537
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Porter County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 174818 |
| Under 18 | 37321 |
| 18–64 | 105544 |
| 65+ | 31953 |
| Median household income | 87972 |
| Poverty rate | 9.58 |
| Homeownership rate | 77.73 |
| Unemployment rate | 4.69 |
| Median home value | 281500 |
| Gini index | 0.4343 |
| Vacancy rate | 5.54 |
| White | 146281 |
| Black | 7813 |
| Asian | 2597 |
| Native | 202 |
| Hispanic/Latino | 20367 |
| Bachelor's or higher | 52232 |

## Districts

- [IN-01](/us/states/in/districts/01.md) — 80% (congressional)
- [IN Senate District 5](/us/states/in/districts/senate/5.md) — 52% (state senate)
- [IN Senate District 4](/us/states/in/districts/senate/4.md) — 28% (state senate)
- [IN House District 4](/us/states/in/districts/house/4.md) — 35% (state house)
- [IN House District 9](/us/states/in/districts/house/9.md) — 14% (state house)
- [IN House District 10](/us/states/in/districts/house/10.md) — 14% (state house)
- [IN House District 19](/us/states/in/districts/house/19.md) — 12% (state house)
- [IN House District 11](/us/states/in/districts/house/11.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
