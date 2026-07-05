---
type: Jurisdiction
title: "Webster County, MO"
classification: county
fips: "29225"
state: "MO"
demographics:
  population: 40500
  population_under_18: 11134
  population_18_64: 22978
  population_65_plus: 6388
  median_household_income: 71155
  poverty_rate: 15.24
  homeownership_rate: 77.45
  unemployment_rate: 3.85
  median_home_value: 228800
  gini_index: 0.4055
  vacancy_rate: 9.87
  race_white: 37143
  race_black: 434
  race_asian: 49
  race_native: 126
  hispanic: 947
  bachelors_plus: 6337
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 0.5806
  - to: "us/states/mo/districts/07"
    rel: in-district
    area_weight: 0.4193
  - to: "us/states/mo/districts/senate/20"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/129"
    rel: in-district
    area_weight: 0.9833
  - to: "us/states/mo/districts/house/141"
    rel: in-district
    area_weight: 0.0166
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Webster County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 40500 |
| Under 18 | 11134 |
| 18–64 | 22978 |
| 65+ | 6388 |
| Median household income | 71155 |
| Poverty rate | 15.24 |
| Homeownership rate | 77.45 |
| Unemployment rate | 3.85 |
| Median home value | 228800 |
| Gini index | 0.4055 |
| Vacancy rate | 9.87 |
| White | 37143 |
| Black | 434 |
| Asian | 49 |
| Native | 126 |
| Hispanic/Latino | 947 |
| Bachelor's or higher | 6337 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 58% (congressional)
- [MO-07](/us/states/mo/districts/07.md) — 42% (congressional)
- [MO Senate District 20](/us/states/mo/districts/senate/20.md) — 100% (state senate)
- [MO House District 129](/us/states/mo/districts/house/129.md) — 98% (state house)
- [MO House District 141](/us/states/mo/districts/house/141.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
