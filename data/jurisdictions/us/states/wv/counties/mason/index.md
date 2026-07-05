---
type: Jurisdiction
title: "Mason County, WV"
classification: county
fips: "54053"
state: "WV"
demographics:
  population: 25043
  population_under_18: 5144
  population_18_64: 14201
  population_65_plus: 5698
  median_household_income: 49761
  poverty_rate: 19.4
  homeownership_rate: 81.84
  unemployment_rate: 3.81
  median_home_value: 120300
  gini_index: 0.4707
  vacancy_rate: 16.16
  race_white: 23915
  race_black: 253
  race_asian: 93
  race_native: 5
  hispanic: 154
  bachelors_plus: 4047
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/wv/districts/senate/4"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/wv/districts/house/18"
    rel: in-district
    area_weight: 0.6646
  - to: "us/states/wv/districts/house/17"
    rel: in-district
    area_weight: 0.3348
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Mason County, WV

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25043 |
| Under 18 | 5144 |
| 18–64 | 14201 |
| 65+ | 5698 |
| Median household income | 49761 |
| Poverty rate | 19.4 |
| Homeownership rate | 81.84 |
| Unemployment rate | 3.81 |
| Median home value | 120300 |
| Gini index | 0.4707 |
| Vacancy rate | 16.16 |
| White | 23915 |
| Black | 253 |
| Asian | 93 |
| Native | 5 |
| Hispanic/Latino | 154 |
| Bachelor's or higher | 4047 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 4](/us/states/wv/districts/senate/4.md) — 100% (state senate)
- [WV House District 18](/us/states/wv/districts/house/18.md) — 66% (state house)
- [WV House District 17](/us/states/wv/districts/house/17.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
