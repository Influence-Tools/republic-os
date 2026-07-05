---
type: Jurisdiction
title: "Worth County, GA"
classification: county
fips: "13321"
state: "GA"
demographics:
  population: 20451
  population_under_18: 4548
  population_18_64: 11734
  population_65_plus: 4169
  median_household_income: 58694
  poverty_rate: 24.04
  homeownership_rate: 73.7
  unemployment_rate: 6.9
  median_home_value: 104900
  gini_index: 0.4389
  vacancy_rate: 17.02
  race_white: 13576
  race_black: 5166
  race_asian: 158
  race_native: 47
  hispanic: 495
  bachelors_plus: 2311
districts:
  - to: "us/states/ga/districts/08"
    rel: in-district
    area_weight: 0.997
  - to: "us/states/ga/districts/senate/13"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ga/districts/house/152"
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

# Worth County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20451 |
| Under 18 | 4548 |
| 18–64 | 11734 |
| 65+ | 4169 |
| Median household income | 58694 |
| Poverty rate | 24.04 |
| Homeownership rate | 73.7 |
| Unemployment rate | 6.9 |
| Median home value | 104900 |
| Gini index | 0.4389 |
| Vacancy rate | 17.02 |
| White | 13576 |
| Black | 5166 |
| Asian | 158 |
| Native | 47 |
| Hispanic/Latino | 495 |
| Bachelor's or higher | 2311 |

## Districts

- [GA-08](/us/states/ga/districts/08.md) — 100% (congressional)
- [GA Senate District 13](/us/states/ga/districts/senate/13.md) — 100% (state senate)
- [GA House District 152](/us/states/ga/districts/house/152.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
