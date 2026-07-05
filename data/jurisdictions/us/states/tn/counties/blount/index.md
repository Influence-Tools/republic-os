---
type: Jurisdiction
title: "Blount County, TN"
classification: county
fips: "47009"
state: "TN"
demographics:
  population: 139333
  population_under_18: 30566
  population_18_64: 41218
  population_65_plus: 67549
  median_household_income: 77365
  poverty_rate: 8.37
  homeownership_rate: 76.99
  unemployment_rate: 3.54
  median_home_value: 320500
  gini_index: 0.4323
  vacancy_rate: 10.23
  race_white: 124360
  race_black: 3553
  race_asian: 1100
  race_native: 131
  hispanic: 6517
  bachelors_plus: 39536
districts:
  - to: "us/states/tn/districts/02"
    rel: in-district
    area_weight: 0.996
  - to: "us/states/tn/districts/senate/2"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/tn/districts/house/8"
    rel: in-district
    area_weight: 0.7816
  - to: "us/states/tn/districts/house/20"
    rel: in-district
    area_weight: 0.2176
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Blount County, TN

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 139333 |
| Under 18 | 30566 |
| 18–64 | 41218 |
| 65+ | 67549 |
| Median household income | 77365 |
| Poverty rate | 8.37 |
| Homeownership rate | 76.99 |
| Unemployment rate | 3.54 |
| Median home value | 320500 |
| Gini index | 0.4323 |
| Vacancy rate | 10.23 |
| White | 124360 |
| Black | 3553 |
| Asian | 1100 |
| Native | 131 |
| Hispanic/Latino | 6517 |
| Bachelor's or higher | 39536 |

## Districts

- [TN-02](/us/states/tn/districts/02.md) — 100% (congressional)
- [TN Senate District 2](/us/states/tn/districts/senate/2.md) — 100% (state senate)
- [TN House District 8](/us/states/tn/districts/house/8.md) — 78% (state house)
- [TN House District 20](/us/states/tn/districts/house/20.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
