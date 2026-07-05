---
type: Jurisdiction
title: "Montgomery County, IA"
classification: county
fips: "19137"
state: "IA"
demographics:
  population: 10214
  population_under_18: 2307
  population_18_64: 5546
  population_65_plus: 2361
  median_household_income: 63666
  poverty_rate: 15.27
  homeownership_rate: 69.14
  unemployment_rate: 2.63
  median_home_value: 121400
  gini_index: 0.4723
  vacancy_rate: 8.39
  race_white: 9411
  race_black: 184
  race_asian: 109
  race_native: 6
  hispanic: 82
  bachelors_plus: 1850
districts:
  - to: "us/states/ia/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/senate/9"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/house/18"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Montgomery County, IA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10214 |
| Under 18 | 2307 |
| 18–64 | 5546 |
| 65+ | 2361 |
| Median household income | 63666 |
| Poverty rate | 15.27 |
| Homeownership rate | 69.14 |
| Unemployment rate | 2.63 |
| Median home value | 121400 |
| Gini index | 0.4723 |
| Vacancy rate | 8.39 |
| White | 9411 |
| Black | 184 |
| Asian | 109 |
| Native | 6 |
| Hispanic/Latino | 82 |
| Bachelor's or higher | 1850 |

## Districts

- [IA-03](/us/states/ia/districts/03.md) — 100% (congressional)
- [IA Senate District 9](/us/states/ia/districts/senate/9.md) — 100% (state senate)
- [IA House District 18](/us/states/ia/districts/house/18.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
