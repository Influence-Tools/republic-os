---
type: Jurisdiction
title: "Wilcox County, GA"
classification: county
fips: "13315"
state: "GA"
demographics:
  population: 8798
  population_under_18: 1671
  population_18_64: 5378
  population_65_plus: 1749
  median_household_income: 54138
  poverty_rate: 21.9
  homeownership_rate: 74.67
  unemployment_rate: 5.54
  median_home_value: 87600
  gini_index: 0.4592
  vacancy_rate: 24.49
  race_white: 5222
  race_black: 2830
  race_asian: 0
  race_native: 25
  hispanic: 331
  bachelors_plus: 1470
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/senate/20"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ga/districts/house/148"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Wilcox County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8798 |
| Under 18 | 1671 |
| 18–64 | 5378 |
| 65+ | 1749 |
| Median household income | 54138 |
| Poverty rate | 21.9 |
| Homeownership rate | 74.67 |
| Unemployment rate | 5.54 |
| Median home value | 87600 |
| Gini index | 0.4592 |
| Vacancy rate | 24.49 |
| White | 5222 |
| Black | 2830 |
| Asian | 0 |
| Native | 25 |
| Hispanic/Latino | 331 |
| Bachelor's or higher | 1470 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 20](/us/states/ga/districts/senate/20.md) — 100% (state senate)
- [GA House District 148](/us/states/ga/districts/house/148.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
