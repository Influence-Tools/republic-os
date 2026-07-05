---
type: Jurisdiction
title: "Amador County, CA"
classification: county
fips: "06005"
state: "CA"
demographics:
  population: 41428
  population_under_18: 6389
  population_18_64: 23616
  population_65_plus: 11423
  median_household_income: 88044
  poverty_rate: 8.19
  homeownership_rate: 80.42
  unemployment_rate: 5.4
  median_home_value: 449800
  gini_index: 0.4459
  vacancy_rate: 15.4
  race_white: 31536
  race_black: 838
  race_asian: 617
  race_native: 512
  hispanic: 6634
  bachelors_plus: 9733
districts:
  - to: "us/states/ca/districts/05"
    rel: in-district
    area_weight: 0.9974
  - to: "us/states/ca/districts/senate/4"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ca/districts/house/1"
    rel: in-district
    area_weight: 0.7923
  - to: "us/states/ca/districts/house/9"
    rel: in-district
    area_weight: 0.2075
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Amador County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 41428 |
| Under 18 | 6389 |
| 18–64 | 23616 |
| 65+ | 11423 |
| Median household income | 88044 |
| Poverty rate | 8.19 |
| Homeownership rate | 80.42 |
| Unemployment rate | 5.4 |
| Median home value | 449800 |
| Gini index | 0.4459 |
| Vacancy rate | 15.4 |
| White | 31536 |
| Black | 838 |
| Asian | 617 |
| Native | 512 |
| Hispanic/Latino | 6634 |
| Bachelor's or higher | 9733 |

## Districts

- [CA-05](/us/states/ca/districts/05.md) — 100% (congressional)
- [CA Senate District 4](/us/states/ca/districts/senate/4.md) — 100% (state senate)
- [CA House District 1](/us/states/ca/districts/house/1.md) — 79% (state house)
- [CA House District 9](/us/states/ca/districts/house/9.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
