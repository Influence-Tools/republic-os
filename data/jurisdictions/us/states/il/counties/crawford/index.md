---
type: Jurisdiction
title: "Crawford County, IL"
classification: county
fips: "17033"
state: "IL"
demographics:
  population: 18511
  population_under_18: 3746
  population_18_64: 11106
  population_65_plus: 3659
  median_household_income: 71674
  poverty_rate: 12.09
  homeownership_rate: 81.94
  unemployment_rate: 3.01
  median_home_value: 121100
  gini_index: 0.4414
  vacancy_rate: 11.41
  race_white: 16763
  race_black: 636
  race_asian: 45
  race_native: 237
  hispanic: 491
  bachelors_plus: 3621
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.9958
  - to: "us/states/il/districts/senate/51"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/il/districts/house/102"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Crawford County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18511 |
| Under 18 | 3746 |
| 18–64 | 11106 |
| 65+ | 3659 |
| Median household income | 71674 |
| Poverty rate | 12.09 |
| Homeownership rate | 81.94 |
| Unemployment rate | 3.01 |
| Median home value | 121100 |
| Gini index | 0.4414 |
| Vacancy rate | 11.41 |
| White | 16763 |
| Black | 636 |
| Asian | 45 |
| Native | 237 |
| Hispanic/Latino | 491 |
| Bachelor's or higher | 3621 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL Senate District 51](/us/states/il/districts/senate/51.md) — 100% (state senate)
- [IL House District 102](/us/states/il/districts/house/102.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
