---
type: Jurisdiction
title: "Haywood County, TN"
classification: county
fips: "47075"
state: "TN"
demographics:
  population: 17475
  population_under_18: 3835
  population_18_64: 9975
  population_65_plus: 3665
  median_household_income: 50472
  poverty_rate: 21.51
  homeownership_rate: 60.65
  unemployment_rate: 5.87
  median_home_value: 152400
  gini_index: 0.4643
  vacancy_rate: 13.23
  race_white: 7568
  race_black: 8561
  race_asian: 21
  race_native: 23
  hispanic: 844
  bachelors_plus: 2303
districts:
  - to: "us/states/tn/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tn/districts/senate/26"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/tn/districts/house/81"
    rel: in-district
    area_weight: 0.7152
  - to: "us/states/tn/districts/house/80"
    rel: in-district
    area_weight: 0.2845
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Haywood County, TN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17475 |
| Under 18 | 3835 |
| 18–64 | 9975 |
| 65+ | 3665 |
| Median household income | 50472 |
| Poverty rate | 21.51 |
| Homeownership rate | 60.65 |
| Unemployment rate | 5.87 |
| Median home value | 152400 |
| Gini index | 0.4643 |
| Vacancy rate | 13.23 |
| White | 7568 |
| Black | 8561 |
| Asian | 21 |
| Native | 23 |
| Hispanic/Latino | 844 |
| Bachelor's or higher | 2303 |

## Districts

- [TN-08](/us/states/tn/districts/08.md) — 100% (congressional)
- [TN Senate District 26](/us/states/tn/districts/senate/26.md) — 100% (state senate)
- [TN House District 81](/us/states/tn/districts/house/81.md) — 72% (state house)
- [TN House District 80](/us/states/tn/districts/house/80.md) — 28% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
