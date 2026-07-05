---
type: Jurisdiction
title: "Barnstable County, MA"
classification: county
fips: "25001"
state: "MA"
demographics:
  population: 231668
  population_under_18: 32704
  population_18_64: 122209
  population_65_plus: 76755
  median_household_income: 95241
  poverty_rate: 7.67
  homeownership_rate: 81.07
  unemployment_rate: 5.02
  median_home_value: 629000
  gini_index: 0.4787
  vacancy_rate: 36.36
  race_white: 198817
  race_black: 6467
  race_asian: 3422
  race_native: 1025
  hispanic: 8561
  bachelors_plus: 129740
districts:
  - to: "us/states/ma/districts/09"
    rel: in-district
    area_weight: 0.3491
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ma]
timestamp: "2026-07-03"
---

# Barnstable County, MA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 231668 |
| Under 18 | 32704 |
| 18–64 | 122209 |
| 65+ | 76755 |
| Median household income | 95241 |
| Poverty rate | 7.67 |
| Homeownership rate | 81.07 |
| Unemployment rate | 5.02 |
| Median home value | 629000 |
| Gini index | 0.4787 |
| Vacancy rate | 36.36 |
| White | 198817 |
| Black | 6467 |
| Asian | 3422 |
| Native | 1025 |
| Hispanic/Latino | 8561 |
| Bachelor's or higher | 129740 |

## Districts

- [MA-09](/us/states/ma/districts/09.md) — 35% (congressional)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
