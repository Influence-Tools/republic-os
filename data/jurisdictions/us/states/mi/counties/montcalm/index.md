---
type: Jurisdiction
title: "Montcalm County, MI"
classification: county
fips: "26117"
state: "MI"
demographics:
  population: 67816
  population_under_18: 14137
  population_18_64: 41566
  population_65_plus: 12113
  median_household_income: 67344
  poverty_rate: 12.55
  homeownership_rate: 83.15
  unemployment_rate: 5.03
  median_home_value: 185500
  gini_index: 0.3997
  vacancy_rate: 12.92
  race_white: 59859
  race_black: 2190
  race_asian: 149
  race_native: 165
  hispanic: 3033
  bachelors_plus: 10178
districts:
  - to: "us/states/mi/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mi/districts/senate/33"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mi/districts/house/91"
    rel: in-district
    area_weight: 0.8504
  - to: "us/states/mi/districts/house/93"
    rel: in-district
    area_weight: 0.1496
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Montcalm County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 67816 |
| Under 18 | 14137 |
| 18–64 | 41566 |
| 65+ | 12113 |
| Median household income | 67344 |
| Poverty rate | 12.55 |
| Homeownership rate | 83.15 |
| Unemployment rate | 5.03 |
| Median home value | 185500 |
| Gini index | 0.3997 |
| Vacancy rate | 12.92 |
| White | 59859 |
| Black | 2190 |
| Asian | 149 |
| Native | 165 |
| Hispanic/Latino | 3033 |
| Bachelor's or higher | 10178 |

## Districts

- [MI-02](/us/states/mi/districts/02.md) — 100% (congressional)
- [MI Senate District 33](/us/states/mi/districts/senate/33.md) — 100% (state senate)
- [MI House District 91](/us/states/mi/districts/house/91.md) — 85% (state house)
- [MI House District 93](/us/states/mi/districts/house/93.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
