---
type: Jurisdiction
title: "Grant County, WA"
classification: county
fips: "53025"
state: "WA"
demographics:
  population: 101799
  population_under_18: 28798
  population_18_64: 58179
  population_65_plus: 14822
  median_household_income: 73267
  poverty_rate: 15.85
  homeownership_rate: 66.28
  unemployment_rate: 6.51
  median_home_value: 299500
  gini_index: 0.4421
  vacancy_rate: 11.98
  race_white: 56828
  race_black: 1345
  race_asian: 1066
  race_native: 1589
  hispanic: 44645
  bachelors_plus: 15153
districts:
  - to: "us/states/wa/districts/04"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/wa/districts/senate/13"
    rel: in-district
    area_weight: 0.9213
  - to: "us/states/wa/districts/senate/16"
    rel: in-district
    area_weight: 0.0787
  - to: "us/states/wa/districts/house/13"
    rel: in-district
    area_weight: 0.9213
  - to: "us/states/wa/districts/house/16"
    rel: in-district
    area_weight: 0.0787
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Grant County, WA

County jurisdiction — 5 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 101799 |
| Under 18 | 28798 |
| 18–64 | 58179 |
| 65+ | 14822 |
| Median household income | 73267 |
| Poverty rate | 15.85 |
| Homeownership rate | 66.28 |
| Unemployment rate | 6.51 |
| Median home value | 299500 |
| Gini index | 0.4421 |
| Vacancy rate | 11.98 |
| White | 56828 |
| Black | 1345 |
| Asian | 1066 |
| Native | 1589 |
| Hispanic/Latino | 44645 |
| Bachelor's or higher | 15153 |

## Districts

- [WA-04](/us/states/wa/districts/04.md) — 100% (congressional)
- [WA Senate District 13](/us/states/wa/districts/senate/13.md) — 92% (state senate)
- [WA Senate District 16](/us/states/wa/districts/senate/16.md) — 8% (state senate)
- [WA House District 13](/us/states/wa/districts/house/13.md) — 92% (state house)
- [WA House District 16](/us/states/wa/districts/house/16.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
