---
type: Jurisdiction
title: "Randolph County, WV"
classification: county
fips: "54083"
state: "WV"
demographics:
  population: 27576
  population_under_18: 5060
  population_18_64: 16225
  population_65_plus: 6291
  median_household_income: 52757
  poverty_rate: 15.91
  homeownership_rate: 74.99
  unemployment_rate: 7.43
  median_home_value: 144800
  gini_index: 0.4557
  vacancy_rate: 18.31
  race_white: 24928
  race_black: 397
  race_asian: 2
  race_native: 23
  hispanic: 308
  bachelors_plus: 5191
districts:
  - to: "us/states/wv/districts/02"
    rel: in-district
    area_weight: 0.9981
  - to: "us/states/wv/districts/senate/11"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wv/districts/house/66"
    rel: in-district
    area_weight: 0.6039
  - to: "us/states/wv/districts/house/67"
    rel: in-district
    area_weight: 0.396
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Randolph County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27576 |
| Under 18 | 5060 |
| 18–64 | 16225 |
| 65+ | 6291 |
| Median household income | 52757 |
| Poverty rate | 15.91 |
| Homeownership rate | 74.99 |
| Unemployment rate | 7.43 |
| Median home value | 144800 |
| Gini index | 0.4557 |
| Vacancy rate | 18.31 |
| White | 24928 |
| Black | 397 |
| Asian | 2 |
| Native | 23 |
| Hispanic/Latino | 308 |
| Bachelor's or higher | 5191 |

## Districts

- [WV-02](/us/states/wv/districts/02.md) — 100% (congressional)
- [WV Senate District 11](/us/states/wv/districts/senate/11.md) — 100% (state senate)
- [WV House District 66](/us/states/wv/districts/house/66.md) — 60% (state house)
- [WV House District 67](/us/states/wv/districts/house/67.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
