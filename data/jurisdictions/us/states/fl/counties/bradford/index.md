---
type: Jurisdiction
title: "Bradford County, FL"
classification: county
fips: "12007"
state: "FL"
demographics:
  population: 27885
  population_under_18: 6259
  population_18_64: 9384
  population_65_plus: 12242
  median_household_income: 63050
  poverty_rate: 16.77
  homeownership_rate: 73.3
  unemployment_rate: 4.72
  median_home_value: 212500
  gini_index: 0.4412
  vacancy_rate: 14.78
  race_white: 20742
  race_black: 4472
  race_asian: 198
  race_native: 18
  hispanic: 1407
  bachelors_plus: 3921
districts:
  - to: "us/states/fl/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/fl/districts/senate/6"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/fl/districts/house/10"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Bradford County, FL

County jurisdiction — 35 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27885 |
| Under 18 | 6259 |
| 18–64 | 9384 |
| 65+ | 12242 |
| Median household income | 63050 |
| Poverty rate | 16.77 |
| Homeownership rate | 73.3 |
| Unemployment rate | 4.72 |
| Median home value | 212500 |
| Gini index | 0.4412 |
| Vacancy rate | 14.78 |
| White | 20742 |
| Black | 4472 |
| Asian | 198 |
| Native | 18 |
| Hispanic/Latino | 1407 |
| Bachelor's or higher | 3921 |

## Districts

- [FL-03](/us/states/fl/districts/03.md) — 100% (congressional)
- [FL Senate District 6](/us/states/fl/districts/senate/6.md) — 100% (state senate)
- [FL House District 10](/us/states/fl/districts/house/10.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
