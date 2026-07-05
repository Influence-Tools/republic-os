---
type: Jurisdiction
title: "Alamance County, NC"
classification: county
fips: "37001"
state: "NC"
demographics:
  population: 176893
  population_under_18: 39209
  population_18_64: 107331
  population_65_plus: 30353
  median_household_income: 65651
  poverty_rate: 13.35
  homeownership_rate: 65.0
  unemployment_rate: 5.06
  median_home_value: 241500
  gini_index: 0.4356
  vacancy_rate: 9.1
  race_white: 106569
  race_black: 34953
  race_asian: 3241
  race_native: 972
  hispanic: 27012
  bachelors_plus: 45835
districts:
  - to: "us/states/nc/districts/09"
    rel: in-district
    area_weight: 0.9989
  - to: "us/states/nc/districts/senate/25"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/64"
    rel: in-district
    area_weight: 0.5491
  - to: "us/states/nc/districts/house/63"
    rel: in-district
    area_weight: 0.4506
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Alamance County, NC

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 176893 |
| Under 18 | 39209 |
| 18–64 | 107331 |
| 65+ | 30353 |
| Median household income | 65651 |
| Poverty rate | 13.35 |
| Homeownership rate | 65.0 |
| Unemployment rate | 5.06 |
| Median home value | 241500 |
| Gini index | 0.4356 |
| Vacancy rate | 9.1 |
| White | 106569 |
| Black | 34953 |
| Asian | 3241 |
| Native | 972 |
| Hispanic/Latino | 27012 |
| Bachelor's or higher | 45835 |

## Districts

- [NC-09](/us/states/nc/districts/09.md) — 100% (congressional)
- [NC Senate District 25](/us/states/nc/districts/senate/25.md) — 100% (state senate)
- [NC House District 64](/us/states/nc/districts/house/64.md) — 55% (state house)
- [NC House District 63](/us/states/nc/districts/house/63.md) — 45% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
