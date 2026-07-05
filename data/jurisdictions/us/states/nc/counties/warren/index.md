---
type: Jurisdiction
title: "Warren County, NC"
classification: county
fips: "37185"
state: "NC"
demographics:
  population: 18795
  population_under_18: 3321
  population_18_64: 10262
  population_65_plus: 5212
  median_household_income: 50638
  poverty_rate: 21.1
  homeownership_rate: 69.36
  unemployment_rate: 7.2
  median_home_value: 154200
  gini_index: 0.5127
  vacancy_rate: 30.5
  race_white: 7220
  race_black: 8882
  race_asian: 25
  race_native: 947
  hispanic: 874
  bachelors_plus: 3622
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/nc/districts/senate/2"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/nc/districts/house/27"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Warren County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18795 |
| Under 18 | 3321 |
| 18–64 | 10262 |
| 65+ | 5212 |
| Median household income | 50638 |
| Poverty rate | 21.1 |
| Homeownership rate | 69.36 |
| Unemployment rate | 7.2 |
| Median home value | 154200 |
| Gini index | 0.5127 |
| Vacancy rate | 30.5 |
| White | 7220 |
| Black | 8882 |
| Asian | 25 |
| Native | 947 |
| Hispanic/Latino | 874 |
| Bachelor's or higher | 3622 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 100% (congressional)
- [NC Senate District 2](/us/states/nc/districts/senate/2.md) — 100% (state senate)
- [NC House District 27](/us/states/nc/districts/house/27.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
