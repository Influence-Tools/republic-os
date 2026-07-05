---
type: Jurisdiction
title: "Polk County, MO"
classification: county
fips: "29167"
state: "MO"
demographics:
  population: 32444
  population_under_18: 7595
  population_18_64: 18918
  population_65_plus: 5931
  median_household_income: 59647
  poverty_rate: 16.3
  homeownership_rate: 71.61
  unemployment_rate: 4.01
  median_home_value: 205800
  gini_index: 0.4538
  vacancy_rate: 10.55
  race_white: 29769
  race_black: 239
  race_asian: 269
  race_native: 82
  hispanic: 970
  bachelors_plus: 6694
districts:
  - to: "us/states/mo/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/128"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Polk County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32444 |
| Under 18 | 7595 |
| 18–64 | 18918 |
| 65+ | 5931 |
| Median household income | 59647 |
| Poverty rate | 16.3 |
| Homeownership rate | 71.61 |
| Unemployment rate | 4.01 |
| Median home value | 205800 |
| Gini index | 0.4538 |
| Vacancy rate | 10.55 |
| White | 29769 |
| Black | 239 |
| Asian | 269 |
| Native | 82 |
| Hispanic/Latino | 970 |
| Bachelor's or higher | 6694 |

## Districts

- [MO-04](/us/states/mo/districts/04.md) — 100% (congressional)
- [MO Senate District 28](/us/states/mo/districts/senate/28.md) — 100% (state senate)
- [MO House District 128](/us/states/mo/districts/house/128.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
