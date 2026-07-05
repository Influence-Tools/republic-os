---
type: Jurisdiction
title: "Moniteau County, MO"
classification: county
fips: "29135"
state: "MO"
demographics:
  population: 15262
  population_under_18: 3877
  population_18_64: 8835
  population_65_plus: 2550
  median_household_income: 65715
  poverty_rate: 10.29
  homeownership_rate: 79.16
  unemployment_rate: 2.54
  median_home_value: 181900
  gini_index: 0.4126
  vacancy_rate: 7.22
  race_white: 13644
  race_black: 342
  race_asian: 72
  race_native: 3
  hispanic: 895
  bachelors_plus: 2114
districts:
  - to: "us/states/mo/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/6"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/58"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Moniteau County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15262 |
| Under 18 | 3877 |
| 18–64 | 8835 |
| 65+ | 2550 |
| Median household income | 65715 |
| Poverty rate | 10.29 |
| Homeownership rate | 79.16 |
| Unemployment rate | 2.54 |
| Median home value | 181900 |
| Gini index | 0.4126 |
| Vacancy rate | 7.22 |
| White | 13644 |
| Black | 342 |
| Asian | 72 |
| Native | 3 |
| Hispanic/Latino | 895 |
| Bachelor's or higher | 2114 |

## Districts

- [MO-03](/us/states/mo/districts/03.md) — 100% (congressional)
- [MO Senate District 6](/us/states/mo/districts/senate/6.md) — 100% (state senate)
- [MO House District 58](/us/states/mo/districts/house/58.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
