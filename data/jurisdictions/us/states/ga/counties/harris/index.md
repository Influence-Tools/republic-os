---
type: Jurisdiction
title: "Harris County, GA"
classification: county
fips: "13145"
state: "GA"
demographics:
  population: 36086
  population_under_18: 7744
  population_18_64: 21402
  population_65_plus: 6940
  median_household_income: 97302
  poverty_rate: 8.98
  homeownership_rate: 88.82
  unemployment_rate: 5.9
  median_home_value: 302800
  gini_index: 0.4136
  vacancy_rate: 11.37
  race_white: 27410
  race_black: 5615
  race_asian: 237
  race_native: 53
  hispanic: 1785
  bachelors_plus: 13699
districts:
  - to: "us/states/ga/districts/03"
    rel: in-district
    area_weight: 0.9939
  - to: "us/states/ga/districts/senate/29"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ga/districts/house/138"
    rel: in-district
    area_weight: 0.7256
  - to: "us/states/ga/districts/house/139"
    rel: in-district
    area_weight: 0.2736
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Harris County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36086 |
| Under 18 | 7744 |
| 18–64 | 21402 |
| 65+ | 6940 |
| Median household income | 97302 |
| Poverty rate | 8.98 |
| Homeownership rate | 88.82 |
| Unemployment rate | 5.9 |
| Median home value | 302800 |
| Gini index | 0.4136 |
| Vacancy rate | 11.37 |
| White | 27410 |
| Black | 5615 |
| Asian | 237 |
| Native | 53 |
| Hispanic/Latino | 1785 |
| Bachelor's or higher | 13699 |

## Districts

- [GA-03](/us/states/ga/districts/03.md) — 99% (congressional)
- [GA Senate District 29](/us/states/ga/districts/senate/29.md) — 100% (state senate)
- [GA House District 138](/us/states/ga/districts/house/138.md) — 73% (state house)
- [GA House District 139](/us/states/ga/districts/house/139.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
